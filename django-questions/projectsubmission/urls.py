from django.urls import path
from . import views

urlpatterns = [
    path('', views.submission_list, name='submission_list'),
    path('submit/', views.project_upload, name='project_upload'),
]
