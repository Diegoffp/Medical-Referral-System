from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path("", views.portal, name="home"),
    path("home/", views.home, name="home_page"),
    path("portal/", views.portal, name="portal"),
    path("listings/", views.listings, name="listings"),
    path("my-referrals/", views.my_referrals, name="my_referrals"),
    path("appointments/", views.appointments, name="appointments"),
    path("create_account/", views.create_account, name="create_account"),
    path("referral/<int:referral_id>/", views.view_referral, name="view_referral"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("edit_account/", views.edit_account, name="edit_account"),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),  
]