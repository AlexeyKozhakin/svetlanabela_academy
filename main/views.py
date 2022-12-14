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
    user_profile = Profile.objects.get(user=request.user)
    courses_list = Course.objects.all()
    course_tab = []
    not_course_tab = []
    enrolled_courses = user_profile.courses.all()
    for element in courses_list:
        if element in enrolled_courses:
            course_tab.append(element)
        else:
            not_course_tab.append(element)
    return render(request, "main/index.html", {
        'profile': user_profile,
        'courses_list': course_tab,
        'not_courses_list': not_course_tab,
    })


@login_required(login_url='/login/')
def profile(request):
    user = User.objects.get(id=request.user.id)
    user_profile = Profile.objects.get(user=user)
    return render(request, "main/profile.html", {
        'profile': user_profile,
    })


@login_required(login_url='/login/')
def course_list(request):
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

    return render(request, "main/course_list.html", {
        'courses_list': courses_list,
        'user': profile,
        'percent_list': percent_list,
    })


@login_required(login_url='/login/')
def course_detail(request, id):
    user_profile = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user_profile)
    course = Course.objects.get(id=id)
    les = Lesson.objects.filter(courses=course)
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

    return render(request, "main/course_detail.html", {
        'user': user_profile,
        'course': course,
        'lessons': les,
        'check': check,
        'boolean': boolean,
        'opened_lessons': opened_lessons,
        'closed_lessons': closed_lessons,
    })


def lesson_detail(request, id_course, id_lesson):
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

    return render(request, "main/lesson_detail.html", {
        'lesson': lesson,
        'boolean': boolean,
        'course': course,
    })


@login_required(login_url='/login/')
def mark_lesson_completed(request, id_course, id_lesson):
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
