from re import L
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def upload_file(request):
    form = UploadFileForm()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file =  form.save(commit=False)
            file.instructor = request.user
            file.save()
            return redirect('home')
        else:
            messages.error(request, 'An error occurred')
    context = {'form':form}
    return render(request, 'Documents/upload.html', context)
