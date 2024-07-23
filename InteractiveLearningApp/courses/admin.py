from django.contrib import admin

from .models import Content, Course, Unit, Lesson

admin.site.register(Course)
admin.site.register(Unit)
admin.site.register(Lesson)
admin.site.register(Content)