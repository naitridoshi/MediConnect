from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
        zip = data.get('zip')
        state = data.get('state')
        city = data.get('city')
        image = request.FILES.get('pic')
        role = data.get('gridRadios2')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, " Username already exists.")
            # context = {'color': 'danger'}
            return render(request, 'login_page.html', context={'color': 'danger'})

        user = User.objects.create(
            username=username,
            first_name=fname,
            last_name=lname,
            email=email,
        )

        user.set_password(password)
        user.save()

        CustomUser.objects.create(
            gender=gender,
            address=address,
            zip=zip,
            state=state,
            city=city,
            image=image,
            role=role
        )

        queryset = CustomUser.objects.all()
        context = {'userData': queryset}
        messages.success(request, "Account registered successfully")
        # context = {'color': 'primary'}
        return render(request, 'login_page.html', context={'color': 'primary'})
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

        if not User.objects.filter(username=username).exists():
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
