from django.shortcuts import render
from .models import Course, Lesson, Profile, User, CheckHomework
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.


@login_required(login_url='/login/')
def index(request):
    user_profile = User.objects.get(id=request.user.id)
    courses_list = Course.objects.all()
    course_tab = []
    not_course_tab = []
    for element in courses_list:
        if element in user_profile.courses.all():
            course_tab.append(element)
        else:
            not_course_tab.append(element)
    return render(request, "main/base.html", {
       'courses_list': course_tab,
        'not_courses_list' : not_course_tab,
        'user': user_profile,
    })


@login_required(login_url='/login/')
def profile_page(request):
    user_profile = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user_profile)
    return render(request, "main/profile.html", {
        'profile': profile,
    })


@login_required(login_url='/login/')
def courses(request):
    user_profile = User.objects.get(id=request.user.id)
    courses_list = Course.objects.all()
    return render(request, "main/courses.html", {
       'courses_list': courses_list,
        'user': user_profile,
    })


@login_required(login_url='/login/')
def course_page(request, id):
    user_profile = User.objects.get(id=request.user.id)
    course = Course.objects.get(id=id)
    les = Lesson.objects.all()
    check = CheckHomework.objects.all()
    boolean = False
    if course in user_profile.courses.all():
        boolean = True

    return render(request, "main/course_template.html", {
        'user': user_profile,
       'course': course,
       'lessons': les,
        'check': check,
        'boolean': boolean,
    })


def lesson_page(request, id):
    lesson = Lesson.objects.get(id=id)
    return render(request, "main/lesson.html", {
        'lesson': lesson,
    })


def admin_page(request):
    courses = Course.objects.all()
    users = User.objects.all()
    return render(request, "main/admin_page.html", {
        'courses': courses,
        'users': users,
    })

