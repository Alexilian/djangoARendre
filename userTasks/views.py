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

# Create your views here.

def task_list(request):
    objets = Task.objects.all().order_by('due_date')
    return render(request, template_name = 'list.html', context = {'objets' : objets})

def objectToTuple():
    listF = []
    for objet in User.objects.all():
        listF.append((objet, objet))
    return tuple(listF)

class TaskForm(forms.Form):
    name = forms.CharField(max_length=250)
    description = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}))
    closed = forms.BooleanField(required=False)
    schedule_date = DateField(widget=SelectDateWidget(years=('2022',)))
    due_date = DateField(widget=SelectDateWidget(years=('2022',)))
    user = forms.CharField(widget=forms.Select(choices=objectToTuple()))
    
    def task(request):
        task_form = TaskForm()
        if request.method == "POST":
            task_form = TaskForm(request.POST)

            if task_form.is_valid():
                task_form = Task.save()
                return render(request ,'addedTask.html', {'form_post':task_form})
        return render(request ,'addTask.html', {'task_form':task_form})
