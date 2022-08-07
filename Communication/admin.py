from django.contrib import admin
from .models import Announcement, Comment, Messages, Replies
# Register your models here.
admin.site.register(Announcement)
admin.site.register(Comment)
admin.site.register(Messages)
admin.site.register(Replies)