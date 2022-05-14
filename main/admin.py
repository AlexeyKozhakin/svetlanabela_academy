# admin Password123!
from django.contrib import admin
from .models import Profile
from main.models import Course, Lesson

# Register your models here.
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Lesson)


