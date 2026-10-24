from django.contrib import admin
from .models import Insurance, Patient, Referral, Location, Provider, AppointmentInfo, Cost

# Register your models here, for Django admin site.
admin.site.register(Insurance)
admin.site.register(Patient)
admin.site.register(Referral)
admin.site.register(Location)
admin.site.register(Provider)
admin.site.register(AppointmentInfo)
admin.site.register(Cost)