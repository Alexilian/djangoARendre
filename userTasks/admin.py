from django.contrib import admin
from userTasks.models import Task, User

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display=('user', 'name', 'creation_date', 'schedule_date', 'due_date')

class UserAdmin(admin.ModelAdmin):
    list_display=('name', 'surname')

admin.site.register(Task, TaskAdmin)
admin.site.register(User, UserAdmin)