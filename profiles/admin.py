from django.contrib import admin
from .models import Profile, CoachProfile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    
@admin.register(CoachProfile)
class CoachProfileAdmin(admin.ModelAdmin):
    list_display = (
        "profile",
        "specialization",
        "experience_years",
        "salary",
    )
