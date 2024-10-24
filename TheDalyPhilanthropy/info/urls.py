from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home2, name="home2"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('mission', views.mission, name="mission"),
]