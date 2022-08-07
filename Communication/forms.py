from cProfile import label
from dataclasses import field
from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import Announcement, Comment, Messages, Replies

class announcementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ['course' , 'title' , 'description']

class commentForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    class Meta:
        model = Comment
        fields = ['body']

class messageForm(ModelForm):
    recipient_username = forms.CharField(label='Recipient Username')
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':50}))
    class Meta:
        model = Messages
        fields = ['recipient_username' , 'body']

class replyForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':60}))
    class Meta:
        model = Replies
        fields = ['body']