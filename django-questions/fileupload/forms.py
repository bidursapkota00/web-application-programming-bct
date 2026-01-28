from django import forms


class FileUploadForm(forms.Form):
    file = forms.FileField(
        error_messages={'required': 'Please select a file to upload!'}
    )

    def clean_file(self):
        file = self.cleaned_data.get('file')

        # Validate file extension
        allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
        file_extension = file.name.split('.')[-1].lower()

        if file_extension not in allowed_extensions:
            raise forms.ValidationError(
                f'Invalid file type. Allowed: {", ".join(allowed_extensions)}'
            )

        # Validate file size (max 2MB)
        max_size = 2 * 1024 * 1024  # 2MB in bytes

        if file.size > max_size:
            raise forms.ValidationError(
                'File size must be less than 2MB'
            )

        return file
