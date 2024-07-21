from django.shortcuts import render, get_object_or_404
from .models import Course, Unit, Lesson, Content

def course(request, slug):
    courses = Course.objects.all()
    units = Unit.objects.all()
    lessons = Lesson.objects.all()
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course': course,
        'courses': courses,
        'units': units,
        'lessons': lessons,
    }
    return render(request, 'courses/course.html', context)


