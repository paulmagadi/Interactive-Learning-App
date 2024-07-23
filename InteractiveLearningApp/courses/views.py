from django.shortcuts import render, get_object_or_404
from .models import Course, Unit, Lesson, Content

def course_view(request, slug):
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
    
    contents = Content.objects.filter(lesson__in=lessons).order_by('lesson', 'order')

    # Prepare contents with split list items
    lesson_contents = {}
    for lesson in lessons:
        lesson_contents[lesson.id] = []
        for content in contents.filter(lesson=lesson):
            if content.content_type == 'list':
                content.split_list_items = content.list_items.split(',')
            lesson_contents[lesson.id].append(content)

    context = {
        'courses': courses,
        'course': course,
        'units': units,
        'selected_unit': selected_unit,
        'lessons': lessons,
        'lesson_contents': lesson_contents,
    }
    return render(request, 'courses/course.html', context)
