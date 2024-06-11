from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new

urlpatterns = [    
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.signout, name="logout"),

    path('tasks/', views.tasks, name="tasks"),
    path('tasks/task_search', views.task_search, name="task_search"),
]  


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #new