from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('COACH', 'Coach'),
        ('STAFF', 'Staff'),
        ('PLAYER', 'Player'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='PLAYER'
    )

    joining_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.role}"

class CoachProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='coach_profile'
    )

    specialization = models.CharField(max_length=100, null=True, blank=True)
    experience_years = models.PositiveIntegerField(null=True, blank=True)
    license_level = models.CharField(max_length=100, null=True, blank=True)

    phone_number = models.CharField(max_length=20, null=True, blank=True)

    resume = models.FileField(upload_to='coach_resumes/', null=True, blank=True)
    signed_contract = models.FileField(upload_to='coach_contracts/', null=True, blank=True)

    parent_occupation = models.CharField(max_length=100, null=True, blank=True)
    parent_contact_number = models.CharField(max_length=20, null=True, blank=True)

    contract_start = models.DateField(null=True, blank=True)
    contract_end = models.DateField(null=True, blank=True)

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Coach Profile - {self.user.username}"
