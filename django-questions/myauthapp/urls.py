from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.student_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.student_register, name='register'),
]
