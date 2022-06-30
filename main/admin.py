# admin Password123!

# tionbec MotDePasse123

from django.contrib import admin
from .models import Profile
from main.models import Course, Lesson, CheckHomework, Progress

# Register your models here.
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CheckHomework)
admin.site.register(Progress)
