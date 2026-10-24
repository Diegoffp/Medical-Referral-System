from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Referral

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

def view_referral(request, referral_id): 
    referral = get_object_or_404(Referral, id=referral_id)
    return render(request, "core/view_referral.html", {"referral": referral})