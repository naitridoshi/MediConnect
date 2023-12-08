from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

ROLE_CHOICES = (
    ('DOCTOR', 'Doctor'),
    ('PATIENT', 'Patient')
)


class CustomUser(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50)
    address = models.TextField(max_length=500)
    zip = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    image = models.ImageField(upload_to="profile")
    role = models.CharField(choices=ROLE_CHOICES, max_length=50)

    def __str__(self):
        return self.email
