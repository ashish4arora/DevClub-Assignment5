from random import choices
from django.contrib.auth.forms import UserCreationForm
from django import forms
from Users.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    CHOICES = [('Student','Student'),('Instructor' , 'Instructor')]
    Status = forms.CharField(widget=forms.RadioSelect(choices = CHOICES))
    first_name = forms.CharField(max_length=15, label = "First Name", required = True)
    last_name = forms.CharField(max_length=15, label = "Last Name")
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'Status')

