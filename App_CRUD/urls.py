from django.urls import path
from . import views_CRUD

urlpatterns = [
    path('CRUD/list/', views_CRUD.employees_list, name='employees-list'),
    path('CRUD/create/', views_CRUD.create_employee, name='create-employee'),
    path('CRUDE/edit/<str:pk>/', views_CRUD.edit_employee, name='edit-employee'),
    path('CRUDE/delete/<str:pk>/', views_CRUD.delete_employee, name='delete-employee'),
]