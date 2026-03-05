from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import CustomUser
from profiles.models import CoachProfile, PlayerProfile, Profile


@receiver(post_save, sender=CustomUser)
def handle_role_profiles(sender, instance, created, **kwargs):

    # Always ensure profile exists
    profile, _ = Profile.objects.get_or_create(user=instance)

    if instance.role == 'COACH':
        CoachProfile.objects.get_or_create(profile=profile)
        PlayerProfile.objects.filter(profile=profile).delete()

    elif instance.role == 'PLAYER':
        PlayerProfile.objects.get_or_create(profile=profile)
        CoachProfile.objects.filter(profile=profile).delete()

    else:
        CoachProfile.objects.filter(profile=profile).delete()
        PlayerProfile.objects.filter(profile=profile).delete()