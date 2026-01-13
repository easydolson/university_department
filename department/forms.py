from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee, AdditionalWork


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'middle_name', 'position',
                  'rate', 'phone', 'email', 'hire_date', 'classroom']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }


class AdditionalWorkForm(forms.ModelForm):
    class Meta:
        model = AdditionalWork
        fields = ['work_type', 'description', 'hours_per_month',
                  'start_date', 'end_date', 'is_active']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']