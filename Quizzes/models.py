from distutils.command.upload import upload
from email.quoprimime import body_check
from django.db import models
from Grades.models import Course

class QuestionBank(models.Model):
    course = models.ForeignKey(Course, related_name="Questions", on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to = "images", null = True, blank = True)
    max_marks = models.IntegerField()

    def __str__(self):
        return self.body[:50]

    class Meta:
        verbose_name = "QuestionBank"
        verbose_name_plural = "QuestionBank"

class Quiz(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, related_name='Quiz', on_delete=models.CASCADE)
    questions = models.ManyToManyField(QuestionBank)
    startDate = models.DateField()
    startTime = models.TimeField()
    endDate = models.DateField()
    endTime = models.TimeField()

    def __str__(self):
        return self.title[:50]
    
    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"
