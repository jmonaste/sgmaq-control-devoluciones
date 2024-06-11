from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # Import the Q object
from django.db.models import Count, Prefetch
from django.db import connection
from .decorators import unauthenticated_user, allowed_user
from .models import Task
from .models import MotivoRechazo


def index(request):
    return render(request, 'global/index.html')

def about(request):
    return render(request, 'global/about.html')

@unauthenticated_user
def signup(request):
    if request.method == 'GET':
        return render(request, 'global/signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'global/signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'global/signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})

@unauthenticated_user
def signin(request):
    if request.method == 'GET':
        return render(request, 'global/signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'global/signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('index')
    
@allowed_user(allowed_roles=['admin', 'manager', 'employee', 'customer'])
def signout(request):
    logout(request)
    return redirect('index')





@login_required
@allowed_user(allowed_roles=['admin', 'manager', 'employee'])
def tasks(request):
    tasks = Task.objects.filter(Q(employee_user=request.user), datecompleted__isnull=True)
    pending_tasks_count = Task.objects.filter(datecompleted__isnull=True).count() # se mostrará para admins y managers
    pending_tasks_per_user = Task.objects.filter(datecompleted__isnull=True).values('employee_user_id__username').annotate(total=Count('id')) # 
    
    # Obtener la descripción del motivo de rechazo para cada tarea
    for task in tasks:
        if task.motivo_rechazo_manager:
            motivo_rechazo_id = task.motivo_rechazo_manager
            motivo_rechazo_desc = MotivoRechazo.objects.get(codigo=motivo_rechazo_id).descripcion
            task.motivo_rechazo_desc = motivo_rechazo_desc  # Añadir el campo de descripción al objeto de tarea


    return render(request, 'tasks/tasks.html', {
        'tasks': tasks,
        'pending_tasks_count': pending_tasks_count,
        'pending_tasks_per_user': pending_tasks_per_user
    })

@login_required
def task_search(request):
    # filtramos las tareas por usuario, por pendiente y por id (patente)
    query = request.GET.get('q')
    tasks = Task.objects.filter(employee_user=request.user, datecompleted__isnull=True, vin__icontains=query)
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })