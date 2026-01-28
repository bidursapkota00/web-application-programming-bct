from django import forms
from django.core.validators import RegexValidator
from django.utils import timezone
from .models import Registration
import re


class RegistrationForm(forms.Form):
    """Registration form with comprehensive validation"""

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    HOBBY_CHOICES = [
        ('football', 'Football'),
        ('tableTennis', 'Table Tennis'),
        ('basketball', 'Basketball'),
    ]

    COUNTRY_CHOICES = [
        ('', '-- Select --'),
        ('Nepal', 'Nepal'),
        ('India', 'India'),
        ('USA', 'USA'),
    ]

    # Name field
    name = forms.CharField(
        max_length=100,
        # error_messages={'required': 'Name is required'}
    )

    # Gender field (Radio buttons)
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
        error_messages={'required': 'Please select gender'}
    )

    # Hobbies field (Checkboxes)
    hobbies = forms.MultipleChoiceField(
        choices=HOBBY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        error_messages={'required': 'Please select at least one hobby'}
    )

    # Appointment field (DateTime)
    appointment = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
        }),
        error_messages={'required': 'Please select appointment'}
    )

    # Country field (Select)
    country = forms.ChoiceField(
        choices=COUNTRY_CHOICES,
        error_messages={'required': 'Please select country'}
    )

    # Email field
    email = forms.EmailField(
        error_messages={
            'required': 'Email is required',
            'invalid': 'Please enter a valid email'
        }
    )

    # Phone field
    phone = forms.CharField(
        max_length=15,
        widget=forms.NumberInput,
        error_messages={'required': 'Phone Number is required'}
    )

    # Resume field (File upload)
    resume = forms.FileField(
        widget=forms.FileInput(attrs={
            'accept': '.pdf,.jpg,.jpeg,.png,.doc,.docx',
        }),
        error_messages={'required': 'Please upload resume'}
    )

    # Password field
    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={'required': 'Password is required'}
    )

    # Confirm Password field
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={'required': 'Confirm Password is required'}
    )

    def clean_appointment(self):
        """Validate appointment is not in the past"""
        appointment = self.cleaned_data.get('appointment')
        now = timezone.now()
        if appointment < now:
            raise forms.ValidationError(
                'Appointment date & time cannot be in the past'
            )
        return appointment

    def clean_phone(self):
        """Validate phone number format (Nepal format)"""
        phone = self.cleaned_data.get('phone')
        # Nepal phone: starts with 9 and 10 digits OR starts with 01 and 8 digits
        phone_regex = r'^(?:9\d{9}|01\d{7})$'
        if not re.match(phone_regex, phone):
            raise forms.ValidationError(
                'Please enter a valid phone number'
            )
        return phone

    def clean_resume(self):
        """Validate resume file type and size"""
        resume = self.cleaned_data.get('resume')
        # Check file extension
        allowed_extensions = ['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx']
        extension = resume.name.split('.')[-1].lower()
        if extension not in allowed_extensions:
            raise forms.ValidationError('Unsupported file format')

        # Check file size (max 2MB)
        max_size = 2 * 1024 * 1024  # 2MB in bytes
        if resume.size > max_size:
            raise forms.ValidationError(
                'File size should be less than 2MB'
            )
        return resume

    def clean_password(self):
        """Validate password strength"""
        password = self.cleaned_data.get('password')
        # At least 8 chars, 1 uppercase, 1 lowercase, 1 digit, 1 symbol
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z\d\s]).{8,}$'
        if not re.match(password_regex, password):
            raise forms.ValidationError(
                'Password must be at least 8 characters long and include '
                'one uppercase letter, one lowercase letter, one number, '
                'and one symbol'
            )
        return password

    def clean(self):
        """Validate confirm password matches password"""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error(
                'confirm_password',
                'Confirm Password did not match Password'
            )

        return cleaned_data
