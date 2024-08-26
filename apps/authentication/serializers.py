from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "slug", "username", "password", "email", "date_joined", "updated_at")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        user_model = self.Meta.model(
            username=self.initial_data["username"], email=self.initial_data["email"]
        )

        try:
            validate_password(value, user_model)
        except ValidationError as e:
            raise ValidationError(e.messages)

        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
        )

        return user
