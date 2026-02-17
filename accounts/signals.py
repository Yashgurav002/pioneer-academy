from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from profiles.models import CoachProfile


@receiver(post_save, sender=CustomUser)
def create_or_update_coach_profile(sender, instance, **kwargs):
    print("Signal triggered for:", instance.username)

    if instance.role == 'COACH':
        print("Role is COACH")

        if hasattr(instance, 'profile'):
            print("Profile exists, creating CoachProfile")

            CoachProfile.objects.get_or_create(
                profile=instance.profile
            )

    else:
        # Optional: If role changes away from COACH,
        # you may delete coach profile automatically
        if hasattr(instance, 'profile'):
            CoachProfile.objects.filter(
                profile=instance.profile
            ).delete()
