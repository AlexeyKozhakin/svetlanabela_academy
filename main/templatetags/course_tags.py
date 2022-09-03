import math

from django import template

from main.models import Progress

register = template.Library()


@register.filter
def course_progress(course, user):
    course_lessons_total = course.lessons.all().count()
    completed_lessons = Progress.objects.get(course=course, user=user).opened_lessons

    completed_lessons_total = completed_lessons.count()
    percentage_progess = int(completed_lessons_total/course_lessons_total * 100)

    return percentage_progess
    
    
