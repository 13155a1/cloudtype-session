from django.contrib import admin 
from django.urls import path, include
from .views import user_email

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('', include('dj_rest_auth.registration.urls')),
    path('user-email/', user_email)
]