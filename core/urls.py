from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("portal/", views.portal, name="portal"),
    path("listings/", views.listings, name="listings"),
    path("appointments/", views.appointments, name="appointments"),
    path("create_account/", views.create_account, name="create_account"),
]