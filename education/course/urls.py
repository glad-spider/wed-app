from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'course'


"""
    path( route , view , kwargs = None , name = None ) 
    route -- который содержит шаблон URL.
    view -- Аргумент является функцией вида или результат as_view()для представлений , основанных на классы
    kwargs -- 
"""
urlpatterns = [
    path('list-courses/', views.CreateCourseViewSet.createcourseList, name='list-courses'),
    path('list-answeres/', views.AnswerViewSet.answerList, name='list-answers'),
    path('list-questions/', views.QuestionViewSet.questionsList, name='list-questions'),
    path('detail/<str:pk>/', views.CreateCourseViewSet.courseDetail, name='course-detail'),
    path('create/', views.CreateCourseViewSet.courseCreate, name='course-create'),
    path('update/<str:pk>', views.CreateCourseViewSet.courseUpdate, name='course-update'),
    path('delete/<str:pk>', views.CreateCourseViewSet.courseDelete, name='course-delete'),

]