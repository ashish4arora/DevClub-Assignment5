from urllib.parse import quote_from_bytes
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import QuestionBank, Quiz
# Register your models here.

class QuizAdmin(ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(QuestionBank)
admin.site.register(Quiz, QuizAdmin)