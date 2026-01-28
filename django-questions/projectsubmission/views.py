from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProjectSubmissionForm
from .models import ProjectSubmission


def project_upload(request):
    if request.method == 'POST':
        form = ProjectSubmissionForm(request.POST, request.FILES)

        if form.is_valid():
            # Check if registration number already exists
            reg_number = form.cleaned_data['tu_registration_number']
            if ProjectSubmission.objects.filter(tu_registration_number=reg_number).exists():
                form.add_error('tu_registration_number',
                               'This registration number already submitted')
                return render(request, 'projectsubmission/project_form.html', {'form': form})

            # Create project submission record
            submission = ProjectSubmission(
                tu_registration_number=reg_number,
                email=form.cleaned_data['email'],
                project_file=form.cleaned_data['project_file'],
            )
            submission.save()

            messages.success(request, 'Project submitted successfully!')
            return redirect('submission_list')
    else:
        form = ProjectSubmissionForm()

    return render(request, 'projectsubmission/project_form.html', {'form': form})


def submission_list(request):
    submissions = ProjectSubmission.objects.all()
    return render(request, 'projectsubmission/submission_list.html', {'submissions': submissions})
