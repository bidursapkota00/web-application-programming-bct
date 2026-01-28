from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_registration, name='user_register'),
    path('', views.user_list, name='user_list'),
]
