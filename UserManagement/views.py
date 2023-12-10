from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password

# User = get_user_model()

# Create your views here.


def register(request):
    if request.method == "POST":
        data = request.POST
        fname = data.get('FName')
        lname = data.get('LName')
        username = data.get('username')
        gender = data.get('gridRadios')
        email = data.get('email')
        password = data.get('password')
        address = data.get('address')
        zipCode = data.get('zip')
        state = data.get('state')
        city = data.get('city')
        image = request.FILES.get('pic')
        role = data.get('gridRadios2')
        confirmPassword = data.get('confirmPassword')

        user = CustomUser.objects.filter(username=username)
        if user.exists():
            messages.error(request, " Username already exists.")
            return redirect('/login')

        hash_password = make_password(password)

        if not check_password(confirmPassword, hash_password):
            messages.error(request, "Both the Passwords do not match.")
            return redirect('/register/')

        # user = CustomUser.objects.create(
        #     username=username,
        #     first_name=fname,
        #     last_name=lname,
        #     email=email,
        # )

        if role == "Patient":
            is_patient = True
            is_doctor = False
        else:
            is_patient = False
            is_doctor = True

        user = CustomUser.objects.create(
            username=username,
            first_name=fname,
            last_name=lname,
            email=email,
            gender=gender,
            address=address,
            zipCode=zipCode,
            state=state,
            city=city,
            image=image,
            role=role,
            is_patient=is_patient,
            is_doctor=is_doctor
        )

        user.set_password(password)
        user.save()

        if is_patient == True:
            Patient.objects.create(user=user)
        else:
            Doctor.objects.create(user=user)

        messages.success(request, "Account registered successfully")
        return redirect('/login/')
    # redirect(reverse('views.login_page', kwargs={ 'color': 'primary' }))
    # else:
    return render(request, 'register.html')


def user(request):
    queryset = CustomUser.objects.all()
    context = {'userData': queryset}

    return render(request, 'user.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username or password')
            return render(request, 'login_page.html', context={'color': 'danger'})

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login_page.html', context={'color': 'danger'})
        else:
            login(request, user)
            return redirect('/dashboard/')
    else:
        return render(request, 'login_page.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url="/login/")
def dashboard(request):
    return render(request, 'dashboard.html')
