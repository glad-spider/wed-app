from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from multiselectfield import MultiSelectField


MY_CHOICES = ((1, 'Item title 1.1'),
              (2, 'Item title 1.2'),
              (3, 'Item title 1.3'),
              (4, 'Item title 1.4'),
              (5, 'Item title 1.5'))

MY_CHOICES2 = ((1, 'Item title 2.1'),
               (2, 'Item title 2.2'),
               (3, 'Item title 2.3'),
               (4, 'Item title 2.4'),
               (5, 'Item title 2.5'))


class MultipleAnswer(models.Model):
    """пользователь выбирает несколько правильнх вариантов"""
    class Meta:
        verbose_name = 'multi ответы'
        verbose_name_plural = 'Несколько ответов'


    my_field = MultiSelectField(choices=MY_CHOICES, max_length=10, max_choices=3)
    my_field2 = MultiSelectField(choices=MY_CHOICES2,  max_choices=3, max_length=10)

    def __str__(self):
        return "{}".format('multi')

class IntegerAnswer(models.Model):
    """пользователь может выбрать числовой ответ"""

    class Meta:
        verbose_name = 'числовые ответы'
        verbose_name_plural = 'числовой ответ'

    class SuitIntNums(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    suitintnums = models.IntegerField(choices=SuitIntNums.choices, default=1)

    def __str__(self):
        return "числовой ответ : {}".format(self.suitintnums)


class SelfAnswer(models.Model):
    """
        пользователь сам описывает ответ на поставленный вопрос
        вводит значение(число / слово)
    """
    class Meta:
        verbose_name = 'Собственные ответы'
        verbose_name_plural = 'Собственный ответ'

    description = models.CharField('описание', max_length=255, blank=False, default=None)

    def __str__(self):
        return "ID[{}], {}...".format(self.id, self.description[0:15])


DEFAULT_INTEGER_ANSWER = 1

DEFAULT_MULTI_ANSWER = 1

DEFAULT_SELF_ANSWER = 1

DEFAULT_USER_ANSWER = ('your answer', 'User answer')


class Answer(models.Model):
    """для каждого вопросы определяем тип ответа"""

    class Meta:
        verbose_name = 'Ответы'
        verbose_name_plural = 'Ответ'

    multi_answer = models.ForeignKey(
        MultipleAnswer, default = None,
        related_name = '+',
        on_delete = models.CASCADE,
        blank = True,
        null = True
    )

    integer_answer = models.ForeignKey(
        IntegerAnswer,
        default = None,
        related_name = '+',
        on_delete = models.CASCADE,
        blank = True,
        null = True
    )
    self_answer = models.ForeignKey(
        SelfAnswer,
        default = None,
        related_name = '+',
        on_delete = models.CASCADE,
        blank = True,
        null = True
    )

    def __str__(self):
        return "ID[{}], Ответ {}".format(self.id, 111)


DEFAULT_ANSWER = 1


class Question(models.Model):
    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопрос'

    description = models.TextField('описнаие', help_text="описание вопроса", default='')

    # шкала сложности вопроса
    LOW, NORMAL, HIGH = 0, 1, 2
    complexity = (
        (LOW, 'low'),
        (NORMAL, 'normal'),
        (HIGH, 'high'),
    )

    complexity = models.IntegerField(choices=complexity,default=LOW)
    answer = models.OneToOneField(
        Answer,
        on_delete=models.CASCADE,
        default=None,
        related_name='+',
        primary_key=True,
    )

    def change_complexity(self): pass

    def __str__(self):
        return "{}, сложность: {}".format(self.description, self.complexity)


DEFAULT_ASK_QUESTION = 1

class CreateCourse(models.Model):
    class Meta:
        verbose_name = 'создание курсов'
        verbose_name_plural = 'создание курса'


    name = models.CharField(
        'назавние курса',
        max_length=50,
        help_text='название курса'
    )
    description = models.TextField(default='', help_text='Описание курса')

    LOW, NORMAL, HIGH = 0, 1, 2
    complexity = (
        (LOW, 'low'),
        (NORMAL, 'normal'),
        (HIGH, 'high'),
    )
    complexity = models.IntegerField(choices=complexity, help_text='сложность')
    num_of_questions = models.CharField(
        'количество вопросов',
        max_length=2,
        help_text='количество вопросов'
    )

    select_questions = models.ForeignKey(
        Question,
        on_delete = models.CASCADE,
        related_name = '+',
        null=True
    )

    def __str__(self):
        return "{}, вопросы: {}, сложность: {}".format(
            self.name,
            self.num_of_questions,
            self.complexity
        )

class CreateCourseAdmin(admin.ModelAdmin):
    """выбор нескольких вопросов"""
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


###



###