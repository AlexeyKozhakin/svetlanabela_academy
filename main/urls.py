from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile_page, name="profile"),
    path("courses/", views.courses, name="courses"),
    path("courses/<int:id>/", views.course_page),
    path("courses/<int:id_course>/<int:id_lesson>/", views.lesson_page),
    # path("lessons/<int:id>/", views.lesson_page),
    path("admin_pannel/", views.admin_page),
    path("courses/<int:id_course>/<int:id_lesson>/action/", views.action),
    ]
