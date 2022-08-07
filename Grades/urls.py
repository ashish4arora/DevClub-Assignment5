from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingView, name = 'landing'),
    path('home/' , views.homeView, name = 'home'),
#     path('courses/', views.courseView, name = 'courses'),
#     path('grades/', views.gradesView , name = 'grades'),
]
