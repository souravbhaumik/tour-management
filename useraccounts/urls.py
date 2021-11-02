from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
]
