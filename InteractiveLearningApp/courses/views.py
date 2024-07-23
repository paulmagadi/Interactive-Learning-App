from django.shortcuts import render, get_object_or_404
from .models import Course, Unit, Lesson

def course(request, slug):
    courses = Course.objects.all()
    course = get_object_or_404(Course, slug=slug)
    units = Unit.objects.filter(course=course)
    unit_slug = request.GET.get('unit')
    selected_unit = None

    if unit_slug:
        selected_unit = get_object_or_404(Unit, slug=unit_slug, course=course)
        lessons = Lesson.objects.filter(unit=selected_unit)
    else:
        lessons = Lesson.objects.filter(unit__course=course)
        

    context = {
        'courses': courses,
        'course': course,
        'units': units,
        'selected_unit': selected_unit,
        'lessons': lessons,
    }
    return render(request, 'courses/course.html', context)
