from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import UserRegistrationForm
from .models import User


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            # Check if email already exists
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'Email already registered')
                return render(request, 'user/user_form.html', {'form': form})

            # Check if username already exists
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already taken')
                return render(request, 'user/user_form.html', {'form': form})

            # Create user record
            user = User(
                full_name=form.cleaned_data['full_name'],
                email=email,
                username=username,
                password=make_password(form.cleaned_data['password']),
            )
            user.save()

            messages.success(request, 'User registered successfully!')
            return redirect('user_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'user/user_form.html', {'form': form})


def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})
