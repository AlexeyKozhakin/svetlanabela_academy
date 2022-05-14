from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return self.name



class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    #course = models.ManyToOneRel()


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # preview_video = models.FileField()


class Progress(models.Model):
    #user = models.ForeignKey()
    #course = models.ForeignKey()
    #opened_lessons = models.ManyToOneRel()
    #passed_lessons = models.ManyToOneRel()
    percent = models.IntegerField()


class CheckHomework(models.Model):
    # user = models.ForeignKey()
    # lesson = models.ForeignKey()
    doneHW = models.BooleanField()


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # body = models.TextField()
    # video = models.FileField()
    courses = models.ManyToManyField(Course, blank=True, related_name="lessons")

