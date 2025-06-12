# website/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    path('home.html', views.home, name='home'),
    path('index.html', views.index, name='index'),
    path('base.html', views.base, name='base'),

]

