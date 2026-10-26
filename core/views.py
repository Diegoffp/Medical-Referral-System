from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib.auth.models import User
from .models import Patient, Referral, Insurance
from django.contrib.auth import authenticate, login


def home(request): 
    return render(request, "core/home.html") 

def portal(request):
    error = None
    if request.method == "POST":
        raw = request.POST.get("referral_number", "").strip().upper()
        digits = raw.replace("REF-", "")
        if digits.isdigit():
            try:
                referral = Referral.objects.get(referral_number=int(digits))
                return redirect("view_referral", referral_id=referral.id)
            except Referral.DoesNotExist:
                pass
        error = "No referral found with that ID."
    return render(request, "core/portal.html",{"error":error})

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

def view_referral(request, referral_id):
    referral = get_object_or_404(Referral, id=referral_id)
    return render(request, "core/view_referral.html", {"referral": referral})

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

    return render(request, "core/Login.html", {"error": error})


