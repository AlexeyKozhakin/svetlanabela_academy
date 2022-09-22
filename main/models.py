from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    preview_video = models.FileField(null=True, blank=True, upload_to="videos/courses/")
        
    def __str__(self):
        return self.title


class Profile(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True, related_name="courses")

    def __str__(self):
        return self.name


# This Video model should hold a reference to the lesson it relates to
# In order to follow the one to many relationship that exists
# But its more appropriate for the user for the lessons to hold the videos field
class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    url = models.URLField(verbose_name="Youtube link")

    def __str__(self):
        return self.title


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    body = models.TextField()
    videos = models.ManyToManyField(Video, related_name="videos", null=True)
    courses = models.ManyToManyField(Course, blank=True, related_name="lessons")

    def __str__(self):
        return self.name


class Progress(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name="progress")
    course = models.ForeignKey(Course, blank=True, on_delete=models.CASCADE, related_name="progress")
    opened_lessons = models.ManyToManyField(Lesson, blank=True, related_name="progress")


class CheckHomework(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name="CheckHomework")
    lesson = models.ForeignKey(Lesson, blank=True, on_delete=models.CASCADE, related_name="CheckHomework")
    mark = models.IntegerField()
