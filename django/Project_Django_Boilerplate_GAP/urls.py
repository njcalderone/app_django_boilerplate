"""Project_Django_Boilerplate_GAP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from App_CRUD import views_CRUD
from Project_Django_Boilerplate_GAP import views

urlpatterns = [
                  path('', views.login, name='login'),
                  path('logout', views.login, name='logout'),
                  path('accounts/profile/', views.profile, name='profile'),
                  path('redirect/', views.redirect, name='redirect'),
                  path('admin/', admin.site.urls),
                  path('accounts/', include('allauth.urls')),
                  path('CRUD/list/', views_CRUD.toas_list, name='toas-list'),
                  path('CRUD/create/', views_CRUD.create_toa, name='create-toa'),
                  path('CRUDE/edit/<str:pk>/', views_CRUD.edit_toa, name='edit-toa'),
                  path('CRUDE/delete/<str:pk>/', views_CRUD.delete_toa, name='delete-toa'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
