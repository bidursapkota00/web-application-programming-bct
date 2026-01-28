from django.db import models


class Student(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.username
