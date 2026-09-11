from django.shortcuts import render 

def home(request): 
    return render(request, "core/home.html") 

def portal(request): 
    return render(request, "core/placeholder.html", {"role": "Portal"}) 

def listings(request): 
    return render(request, "core/placeholder.html", {"role": "Listings"}) 

def appointments(request): 
    return render(request, "core/placeholder.html", {"role": "Appointments"})