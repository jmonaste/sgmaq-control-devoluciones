from django import forms
from django.forms import ModelForm
from .models import Task, PostImage

class UploadFileForm(forms.Form):
    file = forms.FileField()

class EmployeeTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['windows', 'chassis', 'wheels', 'upholstery']
        labels = {
            'windows': 'Ventanas',
            'chassis': 'Carrocería', 
            'wheels': 'Llantas', 
            'upholstery': 'Tapicería'
        }

class TaskUploadImage(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['carimage']