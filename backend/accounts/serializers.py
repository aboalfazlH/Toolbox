
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "is_superuser",
            "date_joined",
            "last_login",
            "phone_number",
        ]
        read_only_fields = [
            "is_staff",
            "is_superuser",
            "date_joined",
            "last_login",
        ]