from django.db import models
from django.conf import settings


class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)

    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} Profile"


class CoachProfile(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        related_name='coach_profile'
    )

    specialization = models.CharField(max_length=100, null=True, blank=True)
    experience_years = models.PositiveIntegerField(null=True, blank=True)
    license_level = models.CharField(max_length=100, null=True, blank=True)

    resume = models.FileField(upload_to='coach_resumes/', null=True, blank=True)
    signed_contract = models.FileField(upload_to='coach_contracts/', null=True, blank=True)

    contract_start = models.DateField(null=True, blank=True)
    contract_end = models.DateField(null=True, blank=True)

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    bio = models.TextField(null=True, blank=True)

    # Parent / Guardian Info (kept as you requested)
    parent_occupation = models.CharField(max_length=100, null=True, blank=True)
    parent_contact_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Coach Profile - {self.profile.user.username}"


class PlayerProfile(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        related_name='player_profile'
    )

    position = models.CharField(max_length=50, null=True, blank=True)
    jersey_number = models.PositiveIntegerField(null=True, blank=True)

    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)

    medical_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Player Profile - {self.profile.user.username}"
