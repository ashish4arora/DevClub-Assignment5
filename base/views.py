from django.shortcuts import render
from Grades.views import courseView, gradesView
# Create your views here.


def home(request):
    context = {}
    return render(request, "base/home.html", context)