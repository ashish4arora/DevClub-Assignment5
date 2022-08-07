from argparse import ONE_OR_MORE
from ctypes import FormatError
from turtle import title
from django.db import models
from Users.models import CustomUser
from Grades.models import Course
# Create your models here.

class Announcement(models.Model):
    course = models.ForeignKey(Course, related_name = 'announcements' , on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    instructor = models.ForeignKey(CustomUser, related_name='announcements', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title 

class Comment(models.Model):
    post = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.author.username + ': ' + self.body[:50]

class Replies(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='replies')
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.author.username + ': ' + self.body[:50]

class Messages(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='messageSent')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='messageReceived')
    recipient_username = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.author.username + ' to ' + self.recipient.username + ' ' + self.body[:50]

