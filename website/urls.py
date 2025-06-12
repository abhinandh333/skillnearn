# website/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('joblist/', views.base, name='joblist'),
]

