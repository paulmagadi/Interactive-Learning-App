# views.py
from django.shortcuts import render
from .models import Lesson, UserProgress

def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons})

def lesson_detail(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    return render(request, 'lessons/lesson_detail.html', {'lesson': lesson})

def user_progress(request):
    progress = UserProgress.objects.get(user=request.user)
    return render(request, 'lessons/user_progress.html', {'progress': progress})
