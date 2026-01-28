from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_note, name='add'),
    path('edit/<int:note_id>/', views.edit_note, name='edit'),
    path('delete/<int:note_id>/', views.delete_note, name='delete'),
]
