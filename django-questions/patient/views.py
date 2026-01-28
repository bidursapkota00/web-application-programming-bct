from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PatientForm
from .models import Patient
import uuid


def patient_registration(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)

        if form.is_valid():
            # Generate patient_id if not provided
            patient_id = form.cleaned_data.get('patient_id')
            if not patient_id:
                patient_id = 'PAT-' + str(uuid.uuid4())[:8].upper()

            # Create patient record
            patient = Patient(
                name=form.cleaned_data['name'],
                patient_id=patient_id,
                mobile=form.cleaned_data['mobile'],
                gender=form.cleaned_data['gender'],
                address=form.cleaned_data.get('address', ''),
                dob=form.cleaned_data['dob'],
                doctor_name=form.cleaned_data['doctor_name'],
            )
            patient.save()

            messages.success(request, 'Patient registered successfully!')
            return redirect('patient_list')
    else:
        form = PatientForm()

    return render(request, 'patient/patient_form.html', {'form': form})


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient/patient_list.html', {'patients': patients})
