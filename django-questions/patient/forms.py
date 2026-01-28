from django import forms
import re


class PatientForm(forms.Form):
    GENDER_CHOICES = [
        ('', '-- Select Gender --'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = forms.CharField(
        max_length=200,
        error_messages={'required': 'Name is required'}
    )

    patient_id = forms.CharField(
        max_length=50,
        required=False
    )

    mobile = forms.CharField(
        max_length=10,
        error_messages={'required': 'Mobile is required'}
    )

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        error_messages={'required': 'Gender is required'}
    )

    address = forms.CharField(
        widget=forms.Textarea,
        required=False
    )

    dob = forms.CharField(
        error_messages={'required': 'Date of Birth is required'}
    )

    doctor_name = forms.CharField(
        max_length=200,
        error_messages={'required': 'Doctor Name is required'}
    )

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']

        mobile_regex = r'^(98|97|96)\d{8}$'
        if not re.match(mobile_regex, mobile):
            raise forms.ValidationError(
                'Mobile must be 10 digits and start with 98, 97 or 96'
            )

        return mobile

    def clean_dob(self):
        dob = self.cleaned_data['dob']

        # Regex for YYYY-MM-DD
        dob_regex = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'

        if not re.match(dob_regex, dob):
            raise forms.ValidationError(
                'Date of Birth must be in YYYY-MM-DD format'
            )

        from datetime import datetime
        try:
            dob_date = datetime.strptime(dob, '%Y-%m-%d').date()
        except ValueError:
            raise forms.ValidationError('Invalid calendar date')

        return dob_date
