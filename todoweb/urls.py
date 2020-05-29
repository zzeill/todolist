from django.urls import path
from . import views

urlpatterns = [
    path('', views.lists, name='lists'),
    path('list/<int:pk>/', views.list_detail, name='list_detail'),
    path('list/new/', views.list_new, name='list_new'),
    path('list/<int:pk>/edit/', views.list_edit, name='list_edit'),
]