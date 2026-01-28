from django.db import models


class ProjectSubmission(models.Model):
    tu_registration_number = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    project_file = models.FileField(upload_to='projects/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tu_registration_number} - {self.email}"
