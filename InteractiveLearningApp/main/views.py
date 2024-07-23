from django.shortcuts import render
from courses.models import Course, Unit, Lesson

def home(request):
    courses = Course.objects.all()
    units = Unit.objects.all()
    lessons = Lesson.objects.all()
    context = {
        'courses': courses,
        'units': units,
        'lessons': lessons,
    }
    return render(request, 'main/index.html', context)

