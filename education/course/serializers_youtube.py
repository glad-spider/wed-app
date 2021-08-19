from rest_framework import serializers
from .models import CreateCourse
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateCourse

        #сериализируем все поля нашей модели
        fields = '__all__'