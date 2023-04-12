from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
