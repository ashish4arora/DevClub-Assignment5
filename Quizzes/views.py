from cmath import log
from datetime import datetime
from pyexpat.errors import messages
from wsgiref.util import request_uri
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import QuestionBank, Quiz
from Grades.models import Course
from . import forms
from django.contrib import messages
import datetime

@login_required(login_url='login')
def makeQuiz(request):
    makequizform = forms.makeQuiz()
    questionbank = QuestionBank.objects.all()
    #------------------------GET REQUEST--------------------------------
    if request.method == "GET":
        querycourse = request.GET.get('CourseCode')
        # print(querycourse)
        if  querycourse != None and querycourse != "":
            querycourse = querycourse.upper()
            bool = Course.objects.filter(coursecode = querycourse).exists()
            if bool != True:
                messages.error(request, "No such course exists")
            else:
                course = Course.objects.get(coursecode = querycourse)
                questionbank = course.Questions.all()
    #-------------------------------------------------------------------

    #-----------------------POST REQUEST--------------------------------
    if request.method == "POST":
        ques = request.POST.getlist('selectedquestions')
        makequizform = forms.makeQuiz(request.POST)
        if makequizform.is_valid():
            formdata = makequizform.save(commit=False)
            # print(formdata)
            formdata.save()
            for quesid in ques:
                quesobj = QuestionBank.objects.get(id = quesid)
                formdata.questions.add(quesobj)
            # print(formdata)
            formdata.save()
            formdata = forms.makeQuiz()
        else:
            messages.error(request, 'An error occured')
        # print(courses)
    #-------------------------------------------------------------------

    context = {'questionbank':questionbank, 'makequizform':makequizform}
    return render(request, 'Quizzes/makeQuiz.html', context)


@login_required(login_url='login')
def quizHome(request):
    context = {}
    if request.user.is_Admin == True or request.user.Status == "Instructor":
        questionbank = QuestionBank.objects.all()
        addquesform = forms.addQuestion()
        if request.method == "POST":
            addquesform = forms.addQuestion(request.POST, request.FILES)
            if addquesform.is_valid():
                addquesform.save()
                addquesform = forms.addQuestion()
            else:
                messages.error(request, 'An error occured')
        context['questionbank'] = questionbank
        context['addquesform'] = addquesform
    if request.user.Status == "Student":
        quizzes = Quiz.objects.filter(course__coursecode__in = request.user.course_students.all()).values()
        print(quizzes)
        context['quizzes'] = quizzes
    return render(request, 'Quizzes/quizHome.html', context)

def quiz(request, quizid):
    quizobj = Quiz.objects.get(id = quizid)

    context = {'quiz':quizobj, 'currdate': datetime.datetime.now().date, 'currtime':datetime.datetime.now().time()}
    return render(request, 'Quizzes/quiz.html', context)