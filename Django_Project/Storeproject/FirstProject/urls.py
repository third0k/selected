from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('aboutour/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]