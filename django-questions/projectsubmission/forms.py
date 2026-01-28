from django import forms


class ProjectSubmissionForm(forms.Form):
    tu_registration_number = forms.CharField(
        max_length=50,
        error_messages={'required': 'TU Registration Number is required'}
    )

    email = forms.EmailField(
        error_messages={
            'required': 'Email Address is required',
            'invalid': 'Please enter a valid email address'
        }
    )

    project_file = forms.FileField(
        error_messages={'required': 'Project File is required'}
    )

    def clean_project_file(self):
        """Validate file type and size"""
        project_file = self.cleaned_data.get('project_file')

        # Allowed file extensions
        allowed_extensions = ['pdf', 'doc',
                              'docx', 'ppt', 'pptx', 'jpeg', 'jpg']
        file_extension = project_file.name.split('.')[-1].lower()

        if file_extension not in allowed_extensions:
            raise forms.ValidationError(
                'File format must be pdf, doc, docx, ppt, pptx, or jpeg'
            )

        # Check file size (max 5MB)
        max_size = 5 * 1024 * 1024  # 5MB in bytes
        if project_file.size > max_size:
            raise forms.ValidationError(
                'File size must be less than 5MB'
            )

        return project_file
