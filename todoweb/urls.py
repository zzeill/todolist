from django.urls import path
from . import views

urlpatterns = [
    path('', views.lists, name='lists'),
    path('list/<int:pk>/', views.list_detail, name='list_detail'),
]