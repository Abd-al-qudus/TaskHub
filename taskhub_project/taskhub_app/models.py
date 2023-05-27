from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


# Create your models here.
class Task(models.Model):
    id = models.TextField(default=str(uuid4()), primary_key=True)
    project_id = models.TextField(default=str(uuid4()))
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']
        
class ProjectModel(models.Model):
    id = models.TextField(default=str(uuid4()), primary_key=True)
    user_id = models.TextField(default=str(uuid4()))
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)