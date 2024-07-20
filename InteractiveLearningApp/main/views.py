from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from courses.models import Course, Unit, Lesson, Content

def home(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'main/index.html', context)