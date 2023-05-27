from django.contrib import admin
from .models import Task, ProjectModel

# Register your models here.
admin.site.register(Task)
admin.site.register(ProjectModel)
