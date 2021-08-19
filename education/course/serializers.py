from rest_framework import fields, serializers
from .models import CreateCourse, Question, Answer


class CreateCourseSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
          model = CreateCourse
          fields = ('name', 'description', 'complexity', 'num_of_questions', 'ask_question')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
          model = Question
          fields = ('description', 'complexity', 'answer')


class AnswerSerializer(serializers.Serializer):
     class Meta:
          model = Answer
          fields = ('multi_answer', 'integer_answer', 'self_answer')


###



###















