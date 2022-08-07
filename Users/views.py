from multiprocessing import context
from django.shortcuts import redirect, render
from . import forms
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password doest not match')

    context = {'page':page}
    return render(request, 'Users/login_register.html' , context)


def registerPage(request):
    page = 'register'
    form = forms.CustomUserCreationForm(initial = {'Status':'Student'})
    if request.method == 'POST':
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An Error has occurred during registration')
    context = {'page':page, 'form':form}
    return render(request, 'Users/login_register.html' , context)

def logoutUser(request):
    logout(request)
    return redirect('home')