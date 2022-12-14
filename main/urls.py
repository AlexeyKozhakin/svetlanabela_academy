from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("courses/", views.course_list, name="course_list"),
    path("courses/<int:id>/", views.course_detail, name="course_detail"),
    path("courses/<int:id_course>/lessons/<int:id_lesson>/", views.lesson_detail, name="lesson_detail"),
    path("courses/<int:id_course>/lessons/<int:id_lesson>/completed/", views.mark_lesson_completed, name="lesson_completed"),
    ]
