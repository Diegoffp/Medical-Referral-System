from django.shortcuts import render, redirect
from .models import Patient, Referral
from django.contrib.auth import authenticate, login

def home(request): 
    return render(request, "core/home.html") 

def portal(request): 
    return render(request, "core/placeholder.html", {"role": "Portal"}) 

def listings(request): 
    referrals = Referral.objects.all()
    return render(request, "core/placeholder.html", {
    "role": "Listings",
    "referrals": referrals
})

def appointments(request): 
    return render(request, "core/placeholder.html", {"role": "Appointments"})

def login_page(request):
    error = "Invalid username or password."
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "Invalid username or password."

    return render(request, "Login.html", {"error": error})
