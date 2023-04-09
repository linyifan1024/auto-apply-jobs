from django.urls import path
from .views import index
urlpatterns = [
    path('', index),
    path('linkedin', index),
    path('glassdoor', index),
    path('indeed', index),
    path('register', index),
]
