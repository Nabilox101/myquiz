from django.urls import path
from . import views



urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.question_quiz_list, name='question_quiz_list'),
    path('quiz/<int:quiz_id>/result/', views.result, name='result'),
]
