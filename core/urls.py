from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("patient/", views.patient_placeholder, name="patient_placeholder"),
    path("provider/", views.provider_placeholder, name="provider_placeholder"),
]
