from django.contrib import admin
from .models import Patient, Referral

# Register your models here, for Django admin site.
admin.site.register(Patient)
admin.site.register(Referral)
