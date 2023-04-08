from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework import generics
from .models import User, Platform, Job
from .serializers import UserSerializer, PlatformSerializer, JobSerializer


# user login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'})
# Create your views here.
class ProfileView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PlatformView(generics.ListAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class JobView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
