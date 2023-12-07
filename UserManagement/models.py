from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

ROLE_CHOICES = (
    ('DOCTOR', 'Doctor'),
    ('PATIENT', 'Patient')
)


class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    address = models.TextField(max_length=500)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    image = models.ImageField(upload_to="profile")
    role = models.CharField(choices=ROLE_CHOICES, max_length=50)

    def __str__(self):
        return self.email
