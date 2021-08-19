from django.contrib import admin
from .models import Profile

#Он не знает о существовании модели Hero, но с помощью двух
#строк кода мы можем сказать это о Hero
admin.site.register(Profile)