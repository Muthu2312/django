from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.CharField(max_length=180)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    completed = models.BooleanField(default=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.task


    
# Restapp/models.py
from django.contrib.auth.models import AbstractUser


class AnotherModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='another_model_entries')
    # Add other fields specific to AnotherModel
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
