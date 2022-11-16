from django.urls import path
from . import views_CRUD

urlpatterns = [
    path('CRUD/list/', views_CRUD.toas_list, name='toas-list'),
    path('CRUD/create/', views_CRUD.create_toa, name='create-toa'),
    path('CRUDE/edit/<str:pk>/', views_CRUD.edit_toa, name='edit-toa'),
    path('CRUDE/delete/<str:pk>/', views_CRUD.delete_toa, name='delete-toa'),
]