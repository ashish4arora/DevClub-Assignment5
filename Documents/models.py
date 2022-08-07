from django.db import models
from Users.models import CustomUser
from Grades.models import Course
# Create your models here.

class Document(models.Model):
    instructor = models.ForeignKey(CustomUser, related_name='documents', on_delete = models.SET_NULL, null = True) 
    course = models.ForeignKey(Course, related_name = 'documents' , on_delete = models.CASCADE)
    file = models.FileField(upload_to= 'uploads')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

