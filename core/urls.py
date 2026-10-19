from django.urls import path
from . import views

urlpatterns = [
    path("", views.port, name="home"),
    path("home/", views.home, name="home_page"),
    path("portal/", views.port, name="portal"),
    path("listings/", views.listings, name="listings"),
    path("appointments/", views.appointments, name="appointments"),
    path("referral/<int:referral_id>/", views.view_referral, name="view_referral"),
]
