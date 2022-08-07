from django.urls import path, include
from . import views

urlpatterns = [
    path('make-announcement', views.makeAnnouncement, name = "makeAnnouncement"),
    path('announcements', views.announcements, name = "announcements"),
    path('replyPost/<str:commentid>' , views.postReply),
    path('announcements/<str:pk>', views.detailedAnnouncement, name = "detailedAnnouncement"),
    path('send-message', views.sendMessage, name = 'sendMessage'),
]
