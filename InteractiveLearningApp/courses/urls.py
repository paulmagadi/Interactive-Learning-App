from django.urls import path
from . import views

urlpatterns = [
    path('course/<str:slug>', views.course, name='course'),
]