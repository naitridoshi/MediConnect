from django.db import models
from django.contrib.auth.models import User, AbstractUser
# from UserManagement.manager import UserManager


# Create your models here.

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

ROLE_CHOICES = (
    ('Doctor', 'Doctor'),
    ('Patient', 'Patient')
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


class Patient(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.role


class Doctor(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Add specific fields related to doctors if needed

    def __str__(self):
        return self.user.role
