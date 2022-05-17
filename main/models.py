from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # preview_video = models.FileField()

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    # course = models.ManyToOneRel(Course, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True, related_name="user")

    def __str__(self):
        return self.username


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # body = models.TextField()
    # video = models.FileField()
    courses = models.ManyToManyField(Course, blank=True, related_name="lessons")

    def __str__(self):
        return self.name


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    opened_lessons = models.IntegerField()
    passed_lessons = models.IntegerField()
    percent = models.IntegerField()


class CheckHomework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    doneHW = models.BooleanField()
