from django.urls import path
# from .views import ProfileView, RegisterUserView
from .views import *


urlpatterns = [
    # path(r'api/users^$', UserCreate.as_view(), name='account-create'),
    path('user', ProfileView.as_view()),
    # path('register/', RegisterUserView.as_view()),
    path('register/', register, name='register'),

]
