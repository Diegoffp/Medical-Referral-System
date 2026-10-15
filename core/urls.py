from django.urls import path 
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("portal/", views.portal, name="portal"),
    path("listings/", views.listings, name="listings"),
    path("appointments/", views.appointments, name="appointments"),
]