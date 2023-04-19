from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework import generics, status
from .models import User, Platform, Job
from .serializers import UserSerializer, PlatformSerializer, JobSerializer, RegisterUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import NewUserForm
from django.contrib import messages
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
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
# class UserCreate(APIView):
#     """ 
#     Creates the user. 
#     """

#     def post(self, request, format='json'):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class AccountsTest(APITestCase):
#     def test_create_user(self):
#         """
#         Ensure we can create a new user and a valid token is created with it.
#         """
#         data = {
#                 'username': 'foobar',
#                 'email': 'foobar@example.com',
#                 'password': 'somepassword'
#                 }

#         response = self.client.post(self.create_url , data, format='json')
#         user = User.objects.latest('id')
#         ...
#         token = Token.objects.get(user=user)
#         self.assertEqual(response.data['token'], token.key)

class ProfileView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PlatformView(generics.ListAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class JobView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    
# class RegisterUserView(generics.CreateAPIView):
#     serializer_class = RegisterUserSerializer
#     def get(self, request, format=None):
#         users = User.objects.all()
#         serializer = self.serializer_class(users, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             name = serializer.data.name
#             email = serializer.data.email
#             password = serializer.data.password
#             confirm_password = serializer.data.confirm_password
#             serializer.save()
            
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            return JsonResponse({'success': False, 'error': 'Passwords do not match'})
        user = User(name=name, email=email, password=password)
        user.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid credentials'})