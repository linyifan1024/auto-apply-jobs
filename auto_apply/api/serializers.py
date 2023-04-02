from rest_framework import serializers
from .models import User, Platform, Job

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        # make password to be hashed
        extra_kwargs = {'password': {'write_only': True}}
        fields =('id', 'name', 'email', 'password', 'created_at', 'updated_at')


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
