from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('aboutour/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dogfood/', views.dogfood, name='dogfood'),
    path('dogtoy/', views.dogtoy, name='dogtoy'),
    path('catfood/', views.catfood, name='catfood'),
    path('cattoy/', views.cattoy, name='cattoy'),
    path('log/', views.log, name='log'),
]