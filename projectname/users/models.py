from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    employee_id = models.CharField(max_length=20, null=True, unique=True,blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    pay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vacation_balance = models.IntegerField(default=0)  # Number of days
    job_title = models.CharField(max_length=100, blank=True, null=True)
    third_party_username = models.CharField(max_length=150, blank=True, null=True)
    third_party_password = models.CharField(max_length=150, blank=True, null=True)  # Consider better security practices!
    agreement_accepted = models.BooleanField(default=False)
    
class ETMInfo(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    etm_username = models.CharField(max_length=100)
    etm_password = models.CharField(max_length=100)  # Seriously, consider better security practices!
    agreement_checked = models.BooleanField(default=False)
    objects = models.Manager()

class EmployeeRecord(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Since 'employee_id' is now a part of CustomUser, we don't need it here.
    wage = models.DecimalField(max_digits=10, decimal_places=2)
    vacation_balance = models.DecimalField(max_digits=10, decimal_places=2)
    total_hours = models.DecimalField(max_digits=10, decimal_places=2)
    reg_hours_pay = models.DecimalField(max_digits=10, decimal_places=2)
    missed_hours_pay = models.DecimalField(max_digits=10, decimal_places=2)
    missed_dates = models.TextField()  # We can store multiple missed dates as text, separated by a comma or any other delimiter.

