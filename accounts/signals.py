from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, CoachProfile


@receiver(post_save, sender=CustomUser)
def create_coach_profile(sender, instance, created, **kwargs):
    if instance.role == 'COACH':
        CoachProfile.objects.get_or_create(user=instance)
