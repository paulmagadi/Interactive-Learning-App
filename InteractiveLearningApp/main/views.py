from django.shortcuts import render
from courses.models import Course, Unit, Lesson, Content

def home(request):
    courses = Course.objects.all()
    units = Unit.objects.all()
    lessons = Lesson.objects.all()
    contents = Content.objects.all()
    context = {
        'courses': courses,
        'units': units,
        'lessons': lessons,
        'contents': contents,
    }
    return render(request, 'main/index.html', context)

