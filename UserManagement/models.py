from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.dispatch import receiver
# from UserManagement.manager import UserManagers
from froala_editor.fields import FroalaField
from .helpers import *


# Create your models here.

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

ROLE_CHOICES = (
    ('Doctor', 'Doctor'),
    ('Patient', 'Patient')
)

CATEGORY_CHOICES = (
    ('Mental Health', 'Mental Health'),
    ('Heart Disease', 'Heart Disease'),
    ('Covid 19', 'Covid 19'),
    ('Immunization', 'Immunization')
)


# class CustomUser(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.SET_NULL, null=True, blank=True)
#     gender = models.CharField(choices=GENDER_CHOICES, max_length=50)
#     address = models.TextField(max_length=500)
#     zip = models.IntegerField(null=False)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     image = models.ImageField(upload_to="profile")
#     role = models.CharField(choices=ROLE_CHOICES, max_length=50)

# def __str__(self):
#     return self.

class CustomUser(AbstractUser):
    # username = models.CharField(unique=True, max_length=100)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50)
    address = models.TextField(max_length=500)
    zipCode = models.IntegerField(null=True)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    image = models.ImageField(upload_to="profile")
    role = models.CharField(choices=ROLE_CHOICES,
                            max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username

    # # USERNAME_FIELD = username
    # REQUIRED_FIELDS = []
    # objects = UserManager()


# class PatientManager(models.Manager):
#     def sync_patients(self):
#         patients = CustomUser.objects.filter(is_patient=True)
#         for patient in patients:
#             patient_instance = self.create(user=patient)


class Patient(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    # objects = PatientManager()

    def __str__(self):
        return self.username


# class DoctorManager(models.Manager):
#     def sync_patients(self):
#         doctors = CustomUser.objects.filter(is_patient=True)
#         for doctor in doctors:
#             doctor_instance = self.create(user=doctor)


class Doctor(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Add specific fields related to doctors if needed
    # objects = DoctorManager()

    def __str__(self):
        return self.user.role


class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blog")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    summary = models.CharField(max_length=1000)
    content = FroalaField()
    draft = models.BooleanField(default=False)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(CustomUser, blank=True, null=True,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)
