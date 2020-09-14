"""employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name = 'Login'),
    path('login', views.login, name = 'Login'),
    path('display', views.display, name = 'display'),
    path('create', views.create, name = 'create'),
    path('registration', views.registration, name = 'registration'),
    path('user_validation', views.registration, name = 'registration'),
    path('change_password', views.change_password, name = 'Change_password'),
    path('delete_account', views.delete_account, name = 'user_delete'),
    path('change_password_page', views.change_password_page, name = 'change_password_page'),
    path('simple_upload', views.simple_upload, name = 'simple_upload')
]
