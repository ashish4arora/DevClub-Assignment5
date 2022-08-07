from email import message
from mimetypes import common_types
from wsgiref.handlers import read_environ
from django.dispatch import receiver
from django.shortcuts import render, redirect
from .forms import announcementForm, messageForm, replyForm
from django.contrib import messages
from Grades.models import Course
from Users.models import CustomUser
from .models import Announcement, Comment, Replies
from . import forms

def makeAnnouncement(request):
    form = announcementForm()
    if request.method == "POST":
        form = announcementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit = False)
            announcement.instructor = request.user
            announcement.save()
            return redirect('announcements')
        else:
            messages.error(request, 'An error occurred')
    context = {'form':form}
    return render(request, 'Communication/make_announcement.html', context)

def announcements(request):
    courses = request.user.course_students.all()
    announcement = []
    for course in courses:
        announcement += course.announcements.all()
    context = {'courses':courses , 'announcements':announcement}
    return render(request, 'Communication/announcements.html', context)

def detailedAnnouncement(request, pk):
    announcement = Announcement.objects.get(id = pk)
    comments = announcement.comments.all()
    commentForm = forms.commentForm()
    replyForm = forms.replyForm()
    if request.method == 'POST':
        commentForm = forms.commentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.post = announcement
            comment.author = request.user
            comment.save()
            commentForm = forms.commentForm()
        else:
            messages.error(request, 'An error occurd in posting comment')
    context = {'announcement':announcement, 'comments':comments, 'commentForm':commentForm, 'replyForm':replyForm}
    return render(request, 'Communication/detailed.html', context)

def sendMessage(request):
    form = messageForm()
    if request.method == "POST":
        form = messageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.recipient_username = message.recipient_username.lower()
            if message.author.username == message.recipient_username:
                messages.error(request, 'Why are you sending messages to youself?')
            else:
                try:
                    recipient = CustomUser.objects.get(username = message.recipient_username)
                    message.recipient = recipient
                    message.save()
                    return redirect('home')
                except:
                    messages.error(request, "Recipient doesn't exist")
        else:
            messages.error(request, 'Error occured in sending the message')
    context = {'form':form}
    return render(request, 'Communication/messages.html' , context)

def postReply(request, commentid):
    if request.method == "POST":
        form = replyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = Comment.objects.get(id = commentid)
            reply.author = request.user
            reply.save()
        else:
            message.error(request, "Recipient doesn't exist")
    # return render('home.html')
    return redirect("../announcements/" + str(Comment.objects.get(id=commentid).post.id))