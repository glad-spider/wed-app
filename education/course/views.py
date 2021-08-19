from rest_framework import viewsets
from .serializers import CreateCourseSerializer, QuestionSerializer, AnswerSerializer
from .models import CreateCourse, Question, Answer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers_youtube import CreateCourseSerializer
from django.shortcuts import get_object_or_404


class CreateCourseViewSet(viewsets.ModelViewSet):

    """
        source: https://www.youtube.com/watch?v=TmsD8QExZ84

    """

    """
        все эти методы нужно достать из класса и работать как с обычными методами
    """
    serializer_class = CreateCourseSerializer
    queryset = CreateCourse.objects.all()

    @api_view(['GET'])
    def createcourseList(self, request):
        # вытащить все объекты
        queryset = CreateCourse.objects.all()

        #сериализируем, передаем объект для сериализации
        serializer = CreateCourseSerializer(queryset, many=True)

        #возращаем JSON
        return Response(serializer.data)

    #@api_view(['GET'])
    def courseDetail(self, reqiest, pk=None):
        queryset = CreateCourse.objects.get(pk)
        course = get_object_or_404(queryset, pk=pk)
        serializer = CreateCourseSerializer(course)
        return Response(serializer.data)

    #@api_view(['POST'])
    def courseCreate(self, request, pk):
        serializer = CreateCourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    #@api_view(['POST'])
    def courseUpdate(self, reqiest, pk):
        courses = CreateCourse.objects.get(pk)
        serializer = CreateCourseSerializer(instance=courses, data=reqiest.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


    """
    должна появиьтся кнопка на уdаleние(сейчас ее нету)
    """
    @api_view(['POST'])
    def courseDelete(self, reqiest, pk):
        courses = CreateCourse.objects.get(pk)
        nm = courses.name
        courses.delete()

        return Response("Success delete course {}".format(nm))


#error
class QuestionViewSet(viewsets.ModelViewSet):
    @api_view(['GET'])
    def questionsList(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class AnswerViewSet(viewsets.ModelViewSet):
    @api_view(['GET'])
    def answerList(self, request):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

###




###

