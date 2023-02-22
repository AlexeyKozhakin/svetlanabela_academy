from django.dispatch import receiver
from django.db.models.signals import m2m_changed

from .models import Profile, Progress


@receiver(m2m_changed, sender=Profile.courses.through)
def create_course_progress(sender, instance, action, **kwargs):
    """
    Create and save a progress instance record for each course assigned to the user's profile
    :param sender:
    :param instance:
    :param action:
    :param kwargs:
    :return:
    """
    if action == "post_add":
        for course in instance.courses.all():
            course_progress, _ = Progress.objects.get_or_create(user=instance.user, course=course)
            # Add the first lesson of the course to the opened_lessons so that user has access to the first lesson
            first_course_lesson = course.lessons.all().first()
            if first_course_lesson is not None:
                course_progress.opened_lessons.add(first_course_lesson)
