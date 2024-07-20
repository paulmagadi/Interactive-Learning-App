from django.shortcuts import render, get_object_or_404
from .models import Course, Unit, Lesson, Content

def course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'courses/course.html', {'course': course})


