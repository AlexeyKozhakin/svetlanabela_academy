from django.db import models
from django.contrib.auth.models import User

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD

# This Video model should hold a reference to the lesson it relates to
# In order to follow the one-to-many relationship that exists
# But its more appropriate for the lessons to hold the videos field
class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to="videos")

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = MarkdownField(rendered_field="parsed_description", validator=VALIDATOR_STANDARD, null=True,
                                blank=True, use_admin_editor=True)
    parsed_description = RenderedMarkdownField(null=True, blank=True, editable=False)
    preview_video = models.ForeignKey(Video, null=True, related_name="preview_video", on_delete=models.SET_NULL)
        
    def __str__(self):
        return self.title


class Profile(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True, related_name="courses")

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    description = MarkdownField(rendered_field="parsed_description", validator=VALIDATOR_STANDARD, null=True, blank=True, use_admin_editor=True)
    parsed_description = RenderedMarkdownField(null=True, blank=True, editable=False)
    body = MarkdownField(rendered_field="parsed_body", validator=VALIDATOR_STANDARD, null=True,
                                blank=True, use_admin_editor=True)
    parsed_body = RenderedMarkdownField(null=True, blank=True, editable=False)
    videos = models.ManyToManyField(Video, related_name="videos")
    courses = models.ManyToManyField(Course, blank=True, related_name="lessons")

    def __str__(self):
        return self.name


class Progress(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name="progress")
    course = models.ForeignKey(Course, blank=True, on_delete=models.CASCADE, related_name="progress")
    opened_lessons = models.ManyToManyField(Lesson, blank=True, related_name="progress")

    def __str__(self):
        return "%s's progress for %s" % (self.user, self.course)

    class Meta:
        verbose_name_plural = "Progresses"
        unique_together = (("user", "course"),)


class CheckHomework(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name="CheckHomework")
    lesson = models.ForeignKey(Lesson, blank=True, on_delete=models.CASCADE, related_name="CheckHomework")
    mark = models.IntegerField()

    def __str__(self):
        return "%s's homework for %s" % (self.user, self.lesson)
