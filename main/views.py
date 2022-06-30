from django.shortcuts import render
from .models import Course, Lesson, Profile, User, CheckHomework, Progress
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect


class Tuple:
    def __init__(self, course, percent):
        self.course = course
        self.percent = percent


# Create your views here.


@login_required(login_url='/login/')
def index(request):
    user_profile = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user_profile)
    courses_list = Course.objects.all()
    course_tab = []
    not_course_tab = []
    for element in courses_list:
        if element in profile.courses.all():
            course_tab.append(element)
        else:
            not_course_tab.append(element)
    return render(request, "main/base.html", {
        'courses_list': course_tab,
        'not_courses_list': not_course_tab,
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
    profile = Profile.objects.get(user=user_profile)
    courses_list = Course.objects.all()
    percent_list = []

    for c in profile.courses.all():
        pro = Progress.objects.get(course=c, user=user_profile)
        tot = c.lessons.all().count()
        ol = pro.opened_lessons.all().count()
        k = Tuple(c, (ol/tot)*100)
        percent_list.append(k)

    return render(request, "main/courses.html", {
        'courses_list': courses_list,
        'user': profile,
        'percent_list': percent_list,
    })


@login_required(login_url='/login/')
def course_page(request, id):
    user_profile = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user_profile)
    course = Course.objects.get(id=id)
    les = Lesson.objects.all()
    check = CheckHomework.objects.all()
    progress = Progress.objects.get(user=user_profile, course=course)
    boolean = False
    opened_lessons = []
    closed_lessons = []
    if course in profile.courses.all():
        boolean = True
        for le in course.lessons.all():
            if le in progress.opened_lessons.all():
                opened_lessons.append(le)
            else:
                closed_lessons.append(le)

    return render(request, "main/course_template.html", {
        'user': user_profile,
        'course': course,
        'lessons': les,
        'check': check,
        'boolean': boolean,
        'opened_lessons': opened_lessons,
        'closed_lessons': closed_lessons,
    })


def lesson_page(request, id_course, id_lesson):
    lesson = Lesson.objects.get(id=id_lesson)
    course = Course.objects.get(id=id_course)
    user_profile = User.objects.get(id=request.user.id)
    progress = Progress.objects.get(course=course, user=user_profile)
    boolean = False
    i = 0

    for les in progress.opened_lessons.all():
        print(i)
        print(progress.opened_lessons.all().count())
        if les == lesson and progress.opened_lessons.all().count()-1 == i:
            boolean = True
            break
        i += 1

    return render(request, "main/lesson.html", {
        'lesson': lesson,
        'boolean': boolean,
        'course': course,
    })


@staff_member_required
def admin_page(request):
    course_list = Course.objects.all()
    users = User.objects.all()
    profiles = Profile.objects.all()
    return render(request, "main/admin_page.html", {
        'courses': course_list,
        'users': users,
        'profiles': profiles,
    })


@login_required(login_url='/login/')
def action(request, id_course, id_lesson):
    lesson = Lesson.objects.get(id=id_lesson)
    user_profile = User.objects.get(id=request.user.id)
    progresses = Progress.objects.filter(user=user_profile)
    for pro in progresses:
        if lesson in pro.opened_lessons.all() and pro.user == user_profile:
            for course in lesson.courses.all():
                if pro.course == course:
                    boolean = False
                    for i in course.lessons.all():
                        if i == lesson:
                            boolean = True
                        elif boolean:
                            pro.opened_lessons.add(i)
                            pro.save()
                            break

    return HttpResponseRedirect("/courses/"+str(id_course)+"/")
