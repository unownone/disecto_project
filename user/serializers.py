from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("full_name","email","phone","address")
        read_only_fields = ("id","is_staff","is_active","date_joined")