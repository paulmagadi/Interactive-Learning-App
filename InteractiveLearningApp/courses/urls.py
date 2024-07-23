from django.urls import path
from . import views

urlpatterns = [
    path('course/<str:slug>', views.course_view, name='course'),
]