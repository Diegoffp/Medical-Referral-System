from django.shortcuts import render 
from .models import Patient, Referral
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required

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

@staff_member_required
def referral_api(request):
    if request.method != "GET":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405,
            headers={"Allow": "GET"}
        )

    referrals = Referral.objects.select_related("patient").all()

    data = []

    for referral in referrals:
        data.append({
            "id": referral.id,
            "patient": f"{referral.patient.first_name} {referral.patient.last_name}",
            "specialty": referral.get_requested_specialty_display(),
            "status": referral.status,
            "date": referral.referral_date.isoformat()
        })

    return JsonResponse({"referrals": data}, status=200)