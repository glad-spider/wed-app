from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

app_name = 'education'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', include('course.urls')),

    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
