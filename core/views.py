from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")


def patient_placeholder(request):
    return render(request, "core/placeholder.html", {"role": "Patient"})


def provider_placeholder(request):
    return render(request, "core/placeholder.html", {"role": "Provider"})
