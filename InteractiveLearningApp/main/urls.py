# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.lesson_list, name='lesson_list'),
    # path('lessons/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    # path('progress/', views.user_progress, name='user_progress'),
]
