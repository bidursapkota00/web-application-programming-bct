from django import forms
import re


class UserRegistrationForm(forms.Form):
    full_name = forms.CharField(
        max_length=40,
        error_messages={
            'required': 'Full name is required',
            'max_length': 'Full name must be up to 40 characters'
        }
    )

    email = forms.EmailField(
        error_messages={
            'required': 'Email is required',
            'invalid': 'Please enter a valid email address'
        }
    )

    username = forms.CharField(
        max_length=100,
        error_messages={'required': 'Username is required'}
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={'required': 'Password is required'}
    )

    def clean_username(self):
        """Validate username: must start with string and followed by number"""
        username = self.cleaned_data.get('username')

        # Pattern: starts with letters, followed by at least one number
        username_regex = r'^[a-zA-Z]+\d+$'
        if not re.match(username_regex, username):
            raise forms.ValidationError(
                'Username must start with letters and end with numbers'
            )

        return username

    def clean_password(self):
        """Validate password length more than 8 characters"""
        password = self.cleaned_data.get('password')

        if len(password) < 8:
            raise forms.ValidationError(
                'Password must be more than 8 characters'
            )

        return password
