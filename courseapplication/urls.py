from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', course_registration, name='course_registration'),
    path('success/', registration_success, name='registration_success'),
    
]

