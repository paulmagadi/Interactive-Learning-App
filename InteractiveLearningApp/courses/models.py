from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_courses')
    learners = models.ManyToManyField(CustomUser, related_name='enrolled_courses', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    
    def save(self, *args, **kwargs):
        self.full_clean()
    
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Course.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            super().save(*args, **kwargs)
       
    def __str__(self):
        return self.title
    
class Unit(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='units')
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    
    def save(self, *args, **kwargs):
        self.full_clean()
    
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Unit.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    class Meta:
        ordering = ['order']

class Lesson(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    
    def save(self, *args, **kwargs):
        self.full_clean()
    
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Lesson.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    def __str__(self):
        return f"{self.unit.title} - {self.title}"

    class Meta:
        ordering = ['order']
        

class Content(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('text', 'Text'),
        ('video', 'Video'),
        ('quiz', 'Quiz'),
    ]

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='contents')
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES)
    text_content = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    quiz_data = models.JSONField(blank=True, null=True)  
    order = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.lesson.title} - {self.get_content_type_display()}"

    class Meta:
        ordering = ['order']

