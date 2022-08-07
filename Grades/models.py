from dis import Instruction
from django.db import models
from Users.models import CustomUser
# Create your models here.


class Course(models.Model):
    coursecode = models.CharField(max_length=6, primary_key=True)
    title = models.CharField(max_length=50)
    instructors = models.ManyToManyField(CustomUser, related_name = 'course_instructors')
    students_enrolled = models.ManyToManyField(CustomUser, related_name = 'course_students')
    credits = models.IntegerField()
    grade = models.CharField(max_length=1, null=True)
    
    def __str__(self):
        return self.title

class Assignment(models.Model):
    title = models.CharField(max_length=50)
    total_marks = models.DecimalField(decimal_places=2, max_digits=5)
    course = models.ForeignKey(Course, related_name='Assignment', on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Grade(models.Model): 
    assignment_id = models.ForeignKey(Assignment, related_name='grade', on_delete=models.CASCADE)
    student = models.ManyToManyField(CustomUser, related_name = 'grade')
    marks = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)

    def percentage(self):
        return (self.marks / self.assignment_id.total_marks) * 100