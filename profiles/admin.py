from django.contrib import admin
from .models import Profile, CoachProfile, PlayerProfile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'created_at')
    search_fields = ('user__username', 'phone')
    

@admin.register(CoachProfile)
class CoachProfileAdmin(admin.ModelAdmin):
    list_display = (
        "profile",
        "specialization",
        "experience_years",
        "salary",
    )
    search_fields = ('profile__user__username', 'specialization')


@admin.register(PlayerProfile)
class PlayerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "profile",
        "position",
        "jersey_number",
        "height",
        "weight",
    )
    search_fields = ('profile__user__username', 'position')
