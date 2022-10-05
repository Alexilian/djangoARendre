from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django import forms
from django.forms import ModelForm
from userTasks.models import Task, User
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect , CheckboxSelectMultiple
from django.forms.widgets import SelectDateWidget
from django.utils import timezone
from datetime import date
from django.forms import ModelForm, DateInput

# Create your views here.

def task_list(request, param1="", param2=""):
    if param1 == "delete":
        Task.objects.get(id=param2).delete()
    objets = Task.objects.all().order_by('due_date')
    return render(request, template_name = 'list.html', context = {'objets' : objets})

def task_detail(request, param):
    objet = Task.objects.get(id=param)
    return render(request, template_name = 'detail.html', context = {'objet' : objet})


def user_list(request, param1="", param2=""):
    if param1 == "delete":
        User.objects.get(id=param2).delete()
    objets = User.objects.all().order_by('name')
    return render(request, template_name = 'users.html', context = {'objets' : objets})


class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Nom"
        self.fields["description"].label = "description"
        self.fields["due_date"].label = "due_date"
        self.fields["schedule_date"].label = "schedule_date"
        self.fields["closed"].label = "closed"
        user = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=User.objects.all(), required=False)

    class Meta:
        model = Task
        fields = ("name", "description", "due_date", "schedule_date", "user", "closed")
        widgets = {
            "due_date": DateInput(),
            "schedule_date": DateInput()
        }
    
def task(request):
    task_form = TaskForm()
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            new_task = task_form.save()
            return render(request, template_name = 'detail.html', context = {'objet' : new_task})
    return render(request ,'addTask.html', {'task_form':task_form})

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Nom"
        self.fields["surname"].label = "Nom de famille"

    class Meta:
        model = User
        fields = ("name", "surname")

def user(request):
    user_form = UserForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            objets = User.objects.all().order_by('name')
            return render(request, template_name = 'users.html', context = {'objets' : objets})
    return render(request ,'addUser.html', {'user_form':user_form})
