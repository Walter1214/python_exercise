from django.db import models
# Create your models here.
from django.utils import timezone


class Account(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ordering = ['created_at']
