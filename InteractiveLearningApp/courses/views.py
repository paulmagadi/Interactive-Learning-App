from django.shortcuts import render, get_object_or_404
from .models import Course, Unit, Lesson, Content

def course(request, slug):
    course = get_object_or_404(Course, id=slug)
    return render(request, 'courses/course.html', {'course': course})

# def lesson_detail(request, lesson_id):
#     lesson = get_object_or_404(Lesson, id=lesson_id)
#     return render(request, 'lesson_detail.html', {'lesson': lesson})
