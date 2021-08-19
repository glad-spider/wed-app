from django.contrib import admin
from .models import *


admin.site.register(CreateCourse, CreateCourseAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(MultipleAnswer)
admin.site.register(IntegerAnswer)
admin.site.register(SelfAnswer)



