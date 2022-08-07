from django.contrib import admin

from Grades.models import Course, Assignment, Grade

# Register your models here.
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Grade)