from django.urls import path
from . import views

urlpatterns = [
    path('quizhome', views.quizHome, name = 'quizHome'),
    path('makequiz', views.makeQuiz, name = "makeQuiz"),
    path('quiz/<int:quizid>' , views.quiz, name = "startQuiz")
]
