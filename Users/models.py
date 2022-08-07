from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=15, primary_key=True)
    Status = models.CharField( max_length=10, default='Student')
    # is_Instructor = models.BooleanField(default=False)
    # is_Student = models.BooleanField(default = False)
    is_Admin = models.BooleanField(default=False)


    def __str__(self):
        return self.username




