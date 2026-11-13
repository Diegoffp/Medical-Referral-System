from django.shortcuts import render, redirect
from .models import Patient, Referral
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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
    error = None
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

def edit_account(request):
    if request.method == "POST":
        user = request.user

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        verify_password = request.POST.get("verify_password")
        avatar = request.FILES.get("avatar")

        if username:
            user.username = username

        if email:
            user.email = email

        if password and password == verify_password:
            user.set_password(password)

        user.save()

        return redirect("home")
return render(request, "edit_account.html")
