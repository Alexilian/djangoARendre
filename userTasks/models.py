from asyncio import format_helpers
from datetime import date, timedelta
from django.db import models
from django.utils import timezone
from django.utils.html import format_html


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name+" "+self.surname

class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    schedule_date = models.DateField(default = timezone.now() + timezone.timedelta(days=7))
    due_date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
