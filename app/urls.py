from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="home"),
    path('apps/<slug:slug>/', views.apps, name='apps'),
    path('web/<slug:slug>/', views.web, name='web'),
    path('startup/<slug:slug>/', views.startup, name='startup')
]
