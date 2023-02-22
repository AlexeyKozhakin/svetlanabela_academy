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
            Progress.objects.get_or_create(user=instance.user, course=course)
