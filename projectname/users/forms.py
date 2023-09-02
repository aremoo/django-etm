from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, ETMInfo

class CustomUserCreationForm(UserCreationForm):
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone_number = forms.CharField(max_length=15, required=True,
                                  widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    employee_id = forms.CharField(max_length=20, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Employee ID'}))
    
    class Meta:
        
        model = CustomUser
        fields = ("username", "email", "phone_number", "employee_id", "password1", "password2")  # Added employee_id


class ETMInfoForm(forms.ModelForm):
    class Meta:
        model = ETMInfo  
        fields = ['etm_username', 'etm_password', 'agreement_checked']
        widgets = {
            'etm_password': forms.PasswordInput(),
            'agreement_checked': forms.CheckboxInput(attrs={'required': True}),
        }
        labels = {
            'etm_username': 'Username',
            'etm_password': 'Password',
        }
