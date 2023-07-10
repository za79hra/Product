from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True, primary_key=True)
    password = models.CharField(max_length=255)
    created_data = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)