from pyexpat import model
from socket import fromshare
from django.forms import ModelForm
from .models import QuestionBank, Quiz
from django import forms

class addQuestion(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    class Meta:
        model = QuestionBank
        fields = '__all__'

class makeQuiz(ModelForm):
    startDate = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
    startTime = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type':'time'}))
    endDate = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
    endTime = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type':'time'}))
    class Meta:
        model = Quiz
        fields = ['title', 'course', 'startDate', 'startTime',  'endDate' , 'endTime']