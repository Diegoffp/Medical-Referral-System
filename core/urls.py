from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.portal, name="home"),
    path("home/", views.home, name="home_page"),
    path("portal/", views.portal, name="portal"),
    path("listings/", views.listings, name="listings"),
    path("appointments/", views.appointments, name="appointments"),
    path("create_account/", views.create_account, name="create_account"),
    path("referral/<int:referral_id>/", views.view_referral, name="view_referral"),
    path("login/", views.login_page, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
