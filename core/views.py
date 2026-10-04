from django.shortcuts import render 
from .models import Patient, Referral

def home(request): 
    return render(request, "core/home.html") 

def portal(request):
    referrals = Referral.objects.all()
    return render(request, "core/portal.html", {"referrals": referrals})

def listings(request): 
    referrals = Referral.objects.all()
    return render(request, "core/placeholder.html", {
    "role": "Listings",
    "referrals": referrals
})

def appointments(request): 
    return render(request, "core/placeholder.html", {"role": "Appointments"})