from django.shortcuts import render, get_object_or_404
from .models import Course, Unit, Lesson, Content

def course(request, slug):
    courses = Course.objects.all()
    course = get_object_or_404(Course, slug=slug)
    units = Unit.objects.filter(course=course)
    
    # Check if a unit is selected via query parameters
    unit_id = request.GET.get('unit')
    if unit_id:
        selected_unit = get_object_or_404(Unit, slug=unit_id)
        lessons = Lesson.objects.filter(unit=selected_unit)
        contents = Content.objects.filter(lesson__in=lessons)
    else:
        selected_unit = None
        lessons = Lesson.objects.filter(unit__in=units)
        contents = Content.objects.filter(lesson__in=lessons)

    context = {
        'courses': courses,
        'course': course,
        'units': units,
        'selected_unit': selected_unit,
        'lessons': lessons,
        'contents': contents,
    }
    return render(request, 'courses/course.html', context)


