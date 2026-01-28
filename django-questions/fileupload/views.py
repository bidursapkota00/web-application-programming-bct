from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FileUploadForm
from .models import UploadedFile


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            # Save file to database
            uploaded_file = UploadedFile(
                file=form.cleaned_data['file']
            )
            uploaded_file.save()

            messages.success(request, 'File uploaded successfully!')
            return redirect('upload_success')
    else:
        form = FileUploadForm()

    return render(request, 'fileupload/upload.html', {'form': form})


def upload_success(request):
    files = UploadedFile.objects.all().order_by('-uploaded_at')
    return render(request, 'fileupload/success.html', {'files': files})
