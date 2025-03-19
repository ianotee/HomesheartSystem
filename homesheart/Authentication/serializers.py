from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User





class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "contact", "role")


class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "contact", "role", "password1", "password2")
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate(self, attrs):
        # Check if passwords match
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match!")

        # Ensure password length is sufficient
        password = attrs.get("password1", "")
        if len(password) < 8:
            raise serializers.ValidationError(
                "Passwords must be at least 8 characters!"
            )

        # Validate role
        if attrs.get("role") not in dict(User.ROLE_CHOICES):
            raise serializers.ValidationError("Invalid role selected!")

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password1")
        validated_data.pop("password2")

        # Create user with hashed password
        user = User.objects.create_user(password=password, **validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        role = data.get("role")

        # Authenticate user
        user = authenticate(username=email, password=password)
        if user and user.is_active:
            # Check if role matches
            if user.role != role:
                raise serializers.ValidationError("Incorrect role for the user!")
            return user
        raise serializers.ValidationError("Invalid email or password!")
