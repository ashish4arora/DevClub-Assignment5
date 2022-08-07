from django.shortcuts import redirect, render
from .models import Course, Assignment, Grade
from Documents.models import Document
from django.contrib.auth.decorators import login_required
from .forms import createCourse
from django.contrib import messages
from Communication.models import Messages
from django.db.models import Q
from Documents.models import Document
# Create your views here.

def landingView(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')


@login_required(login_url='login')
def homeView(request):
    user = request.user
    courses = Course.objects.filter(students_enrolled = user)
    grades = Grade.objects.filter(student = user)

    #---- course form----
    form = createCourse()
    if request.user.is_Admin:
        if request.method == "POST":
            form = createCourse(request.POST)
            if form.is_valid():
                form.save()
                form = createCourse()
                redirect('home')
            else:
                messages.error(request, 'Error occured while adding the course')
    #-------------------
    messageReceived = Messages.objects.filter(Q(author = user) | Q(recipient = user))
    context = {'courses' : courses, 'grades':grades, 'status': user.Status, 'courseForm' : form, 'messagesReceived': messageReceived}
    return render(request, 'Grades/home.html' , context)
