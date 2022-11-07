from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class AuthValidateSerializers(serializers.Serializer):
    username = serializers.CharField(min_length=5, max_length=100)
    password = serializers.CharField(min_length=1)


class RegisValidateSeializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


    def validate_username(self, username):
        if User.objects.filter(username=username).count()>0:
            raise ValidationError('User already exists')
        return username