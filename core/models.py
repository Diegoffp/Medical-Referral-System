from django.db import models
from django.conf import settings

# Database model/table creation
# Primary key IDs are handled by Django with auto-incrementing integer
# Django User Model (staff/admin included)
# Attributes: username, password, email, first name, last name, is_staff, is_active, is_superuser, 
#             last_login, date_joined, groups, user_permissions

# Global types used by multiple entities
INSURANCE_TYPES = [('Kaiser Permanente', 'Kaiser Permanente'), ('IEHP', 'IEHP'), ('Medicare', 'Medicare'), ('Medi-Cal', 'Medi-Cal'),
                   ('Blue Shield', 'Blue Shield'), ('Anthem Blue Cross', 'Anthem Blue Cross'), ('Aetna', 'Aetna')]

SPECIALTY_TYPES = [('Cardiology','Cardiology'), ('Orthopedics','Orthopedics'), ('Dermatology','Dermatology'), 
                   ('Neurology','Neurology'), ('Podiatry','Podiatry')]

# Insurance Database Model
# Attributes: name
# String representation: insurance name
class Insurance(models.Model):
    # Attributes
    name = models.CharField(max_length=50, choices=INSURANCE_TYPES, unique=True)

    def __str__(self):
        return self.name

# Patient Database Model
# Attributes: first name, last name, dob, phone #, insurance
# String representation: first name, last name
class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=50)
    insurance = models.ForeignKey(Insurance, on_delete=models.SET_NULL, null=True, related_name='patients')
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# Referral Database Model
# Attributes: referral date, referral_number, requested specialty, status
# String representation: REF-#
class Referral(models.Model):
    STATUS_TYPES = [('Ready','Ready'),('Accepted','Accepted')]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='referrals')
    referral_date = models.DateField()
    referral_number = models.PositiveIntegerField(unique=True)
    requested_specialty = models.CharField(max_length=50, choices=SPECIALTY_TYPES, null=True)
    status = models.CharField(max_length=15, choices=STATUS_TYPES, default='Ready')

    def __str__(self):
        return f"REF-{self.referral_number:06d}"

# Provider Database Model
# Attributes: credentials, first_name, last_name, specialty, accepted_insurance
# String representation: CREDENTIAL_TYPE, last_name
class Provider(models.Model):
    CREDENTIAL_TYPES = [('MD', 'MD'), ('DO', 'DO'), ('NP', 'NP'), ('PA', 'PA')]
    
    credentials = models.CharField(max_length=25, choices=CREDENTIAL_TYPES) 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=50, choices=SPECIALTY_TYPES)
    accepted_insurance = models.ManyToManyField(Insurance, related_name='providers')

    def __str__(self):
            return f"{self.credentials} {self.last_name}"       

# AppointmentInfo Database Model
# Attributes: wait_time
# String representation: provider details, wait time
class AppointmentInfo(models.Model):
    TIME_TYPES = [('Same Day','Same Day'), ('One Day','One Day'), ('Two Days','Two Days'), ('Three Days','Three Days'), 
                  ('Four Days','Four Days'), ('Five Days','Five Days'), ('Six Days','Six Days'), ('One Week','One Week'),
                  ('Two Weeks','Two Weeks'), ('Three Weeks','Three Weeks')]
     
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    wait_time = models.CharField(max_length=25, choices=TIME_TYPES)

    def __str__(self):
                    return f"{self.provider.specialty} {self.provider.credentials} {self.provider.last_name} {self.wait_time}"

# Cost Database Model
# Attributes: expected_cost
# String representation: AppointmentInfo string, insurance, cost 
class Cost(models.Model):
    COST_TYPES = [('$0', '$0'), ('$35', '$35'), ('$65', '$65'), ('$85', '$85'),
                  ('$100', '$100'), ('$150', '$150'), ('$275', '$275')]
    
    appointment_info = models.ForeignKey(AppointmentInfo, on_delete=models.CASCADE)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    expected_cost = models.CharField(max_length=15, choices=COST_TYPES)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['appointment_info', 'insurance'], 
                      name='unique_appointment_insurance_cost')]
    def __str__(self):
                return f"{self.appointment_info} - {self.insurance} - {self.expected_cost}"       