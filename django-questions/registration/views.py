from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import RegistrationForm
from .models import Registration


def registration_form(request):
    """Handle registration form display and submission"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            # Get cleaned data
            data = form.cleaned_data

            # Create registration instance
            registration = Registration(
                name=data['name'],
                gender=data['gender'],
                hobbies=data['hobbies'],
                appointment=data['appointment'],
                country=data['country'],
                email=data['email'],
                phone=data['phone'],
                resume=data['resume'],
                password=make_password(data['password']),  # Hash password
            )
            registration.save()

            messages.success(request, 'Form submitted successfully!')
            return redirect('registration:form')
    else:
        form = RegistrationForm()

    return render(request, 'registration/form.html', {'form': form})
