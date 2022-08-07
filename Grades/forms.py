from django.forms import ModelForm
from django import forms
from .models import Course

class createCourse(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'