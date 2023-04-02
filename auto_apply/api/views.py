from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import User, Platform, Job
from .serializers import UserSerializer, PlatformSerializer, JobSerializer


# Create your views here.
class ProfileView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    