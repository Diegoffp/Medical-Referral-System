from django.db import models
from django.conf import settings

# Database model/table creation
# Primary key IDs are handled by Django with auto-incrementing integer
# Django User Model (staff/admin included)
# Attributes: username, password, email, first name, last name, is_staff, is_active, is_superuser, 
#             last_login, date_joined, groups, user_permissions

# Patient Database Model
# Attributes: first name, last name, dob, phone #, insurance type
# String representation: first name, last name
class Patient(models.Model):
    INSURANCE_TYPES = [("KAISER", "Kaiser Permanente"), ("IEHP", "IEHP"), 
                       ("MEDICARE", "Medicare"), ("MEDI_CAL", "Medi-Cal")]
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=50)

    insurance = models.CharField(max_length=50, choices=INSURANCE_TYPES, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# Referral Database Model
# Attributes: referral date, requested specialty
# String representation: REF-#
class Referral(models.Model):
    SPECIALTY_TYPES = [('CARDIOLOGY','Cardiology'), ('ORTHOPEDICS','Orthopedics'), ('DERMATOLOGY','Dermatology'), 
                       ('NEUROLOGY','Neurology'), ('PODIATRY','Podiatry')]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    referral_date = models.DateField()
    referral_number = models.PositiveIntegerField(unique=True, null=True)
    request_specialty = models.CharField(max_length=50, choices=SPECIALTY_TYPES)

    def __str__(self):
        return f"REF-{self.referral_number:06d}"

# Provider Database Model
# Attributes: credentials, first_name, last_name, specialty
# String representation: CREDENTIAL_TYPE, last_name
class Provider(models.Model):
    CREDENTIAL_TYPES = [("MD", "MD"), ("DO", "DO"), ("NP", "NP"), ("PA", "PA")]
    SPECIALTY_TYPES = [('CARDIOLOGY','Cardiology'), ('ORTHOPEDICS','Orthopedics'), ('DERMATOLOGY','Dermatology'), 
                       ('NEUROLOGY','Neurology'), ('PODIATRY','Podiatry')]
    
    credentials = models.CharField(max_length=25, choices=CREDENTIAL_TYPES) 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=50, choices=SPECIALTY_TYPES)

    def __str__(self):
            return f"{self.credentials} {self.last_name}"       
