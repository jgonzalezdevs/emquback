from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

from management.models import Device


class RegisterSerializer(serializers.ModelSerializer):
    user = get_user_model()
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=user.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        user = get_user_model()
        model = user
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = get_user_model()
        user = user.objects.create(
            email=validated_data['email'],
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'