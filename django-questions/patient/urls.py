from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.patient_registration, name='patient_register'),
    path('', views.patient_list, name='patient_list'),
]
