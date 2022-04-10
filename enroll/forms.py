#from django.core import validators
from django import forms
from django.forms import widgets
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields =['name','email','dob','age']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'})
            

        }

