from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import transaction
from profiles.models import Profile, CoachProfile

User = get_user_model()


# 🔹 READ SERIALIZER (For list/detail)
class CoachReadSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='profile.user.username')
    email = serializers.EmailField(source='profile.user.email')
    phone = serializers.CharField(source='profile.phone')

    class Meta:
        model = CoachProfile
        fields = [
            'id',
            'username',
            'email',
            'phone',
            'specialization',
            'experience_years',
            'license_level',
            'salary',
            'contract_start',
            'contract_end',
            'bio'
        ]


# 🔹 WRITE SERIALIZER (For create/update)
class CoachWriteSerializer(serializers.ModelSerializer):

    # User fields
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    # Profile fields
    phone = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = CoachProfile
        fields = [
            'username',
            'email',
            'password',
            'phone',
            'address',
            'specialization',
            'experience_years',
            'license_level',
            'salary',
            'contract_start',
            'contract_end',
            'bio'
        ]

    @transaction.atomic
    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        phone = validated_data.pop('phone', None)
        address = validated_data.pop('address', None)

    # 1️⃣ Create User (this triggers profile + coachprofile signals)
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role='COACH'
        )

        # 2️⃣ Get profile created by signal
        profile = user.profile

        # Update base profile fields
        profile.phone = phone
        profile.address = address
        profile.save()

        # 3️⃣ Get CoachProfile created by signal
        coach_profile = profile.coach_profile

        # Update coach-specific fields
        for attr, value in validated_data.items():
            setattr(coach_profile, attr, value)

        coach_profile.save()
        return coach_profile