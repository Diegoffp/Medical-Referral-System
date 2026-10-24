from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.models import User
from .models import Patient, Referral, Insurance

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

def create_account(request):
    insurance_options = Insurance.objects.all()

    if request.method == "POST":
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        date_of_birth = request.POST.get("date_of_birth")
        phone_number = request.POST.get("phone_number", "").strip()
        email = request.POST.get("email", "").strip()
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        insurance_name = request.POST.get("insurance")

        if password != confirm_password:
            return render(request, "core/create_account.html", {
                "error": "Passwords do not match.",
                "insurance_options": insurance_options,
            })

        if User.objects.filter(username=username).exists():
            return render(request, "core/create_account.html", {
                "error": "Username already exists.",
                "insurance_options": insurance_options,
            })

        try:
            insurance = Insurance.objects.get(name=insurance_name)
        except Insurance.DoesNotExist:
            return render(request, "core/create_account.html", {
                "error": "Please select a valid insurance option.",
                "insurance_options": insurance_options,
            })

        try:
            with transaction.atomic():
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                )

                Patient.objects.create(
                    user=user,
                    first_name=first_name,
                    last_name=last_name,
                    date_of_birth=date_of_birth,
                    phone_number=phone_number,
                    insurance=insurance,
                )
        except Exception:
            return render(request, "core/create_account.html", {
                "error": "We couldn't create your account. Please check your information and try again.",
                "insurance_options": insurance_options,
            })

        return redirect("home")

    return render(request, "core/create_account.html", {
        "insurance_options": insurance_options,
    })