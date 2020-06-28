from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('applying.html', views.applying, name="applying"),
    path('community.html', views.community, name="community"),
    path('about.html', views.about, name="about"),
    path('jobs.html', views.jobs, name="jobs"),
    path('appointment.html', views.appointment, name="appointment"),

]
