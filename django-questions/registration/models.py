from django.db import models


class Registration(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    HOBBY_CHOICES = [
        ('football', 'Football'),
        ('tableTennis', 'Table Tennis'),
        ('basketball', 'Basketball'),
    ]

    COUNTRY_CHOICES = [
        ('', '-- Select --'),
        ('Nepal', 'Nepal'),
        ('India', 'India'),
        ('USA', 'USA'),
    ]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    hobbies = models.JSONField(default=list)  # Store multiple hobbies as JSON
    appointment = models.DateTimeField()
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resumes/')
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
