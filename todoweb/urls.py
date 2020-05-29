from django.urls import path
from . import views

urlpatterns = [
    path('', views.lists, name='lists'),
    path('list/<int:pk>/', views.list_detail, name='list_detail'),
    path('list/new/', views.list_new, name='list_new'),
    path('list/<int:pk>/edit/', views.list_edit, name='list_edit'),
    path('list/<int:pk>/delete/', views.list_remove, name='list_remove'),
    path('list/<int:pk>/activity/add/', views.add_activity, name='add_activity'),
    path('list/<int:pk>/activity/done/', views.activity_done, name='activity_done'),
    path('list/<int:pk>/activity/remove/', views.activity_remove, name='activity_remove'),
    path("accounts/register", views.register, name="register"),
]