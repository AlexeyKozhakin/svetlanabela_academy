# admin Password123!
# titi Titi220601
# bidule AzertyDemon22
# tionbec MotDePasse123
# jsp JENEsaispas

from django.contrib import admin
from .models import Profile
from main.models import Course, Lesson, CheckHomework, Progress, Video

# Register your models here.
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CheckHomework)
admin.site.register(Progress)
admin.site.register(Video)
