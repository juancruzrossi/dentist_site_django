from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contacto/', views.contact, name="contact"),
    path('sobre_nosotros/', views.about, name="about"),
    path('servicios/', views.service, name="service"),
    path('turnos/', views.appointment, name="appointment"),
]