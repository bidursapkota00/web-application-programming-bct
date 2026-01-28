from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import Student


def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(username=username)
            # Check hashed password
            if check_password(password, student.password):
                request.session['student_id'] = student.id
                request.session['student_name'] = student.name
                return redirect('dashboard')
            else:
                return render(request, 'testapp/login.html', {
                    'error': 'Invalid username/password'
                })
        except Student.DoesNotExist:
            return render(request, 'testapp/login.html', {
                'error': 'Invalid username/password'
            })

    return render(request, 'testapp/login.html')


def dashboard(request):
    # Check if student is logged in
    if 'student_id' not in request.session:
        return redirect('login')

    student_name = request.session.get('student_name')
    return render(request, 'testapp/dashboard.html', {'name': student_name})


def logout(request):
    # Clear session
    request.session.flush()
    return redirect('login')


def student_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        name = request.POST.get('name')
        email = request.POST.get('email')

        # Validation
        if not username or not password or not confirm_password or not name or not email:
            return render(request, 'testapp/register.html', {
                'error': 'All fields are required'
            })

        if password != confirm_password:
            return render(request, 'testapp/register.html', {
                'error': 'Passwords do not match'
            })

        # Check if username already exists
        if Student.objects.filter(username=username).exists():
            return render(request, 'testapp/register.html', {
                'error': 'Username already exists'
            })

        # Check if email already exists
        if Student.objects.filter(email=email).exists():
            return render(request, 'testapp/register.html', {
                'error': 'Email already registered'
            })

        # Create new student with hashed password
        Student.objects.create(
            username=username,
            password=make_password(password),
            name=name,
            email=email
        )

        return render(request, 'testapp/register.html', {
            'success': 'Account created successfully! You can now login.'
        })

    return render(request, 'testapp/register.html')
