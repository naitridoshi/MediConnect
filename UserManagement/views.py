from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def register(request):
    if request.method == "POST":
        data = request.POST
        fname = data.get('FName')
        lname = data.get('LName')
        gender = data.get('gridRadios')
        email = data.get('email')
        password = data.get('password')
        address = data.get('address')
        country = data.get('country')
        state = data.get('state')
        city = data.get('city')
        image = request.FILES.get('pic')
        role = data.get('gridRadios2')

        User.objects.create(
            fname=fname,
            lname=lname,
            gender=gender,
            email=email,
            password=password,
            address=address,
            country=country,
            state=state,
            city=city,
            image=image,
            role=role
        )

        queryset = User.objects.all()
        context = {'userData': queryset}
        return render(request, 'user.html', context)
    else:
        return render(request, 'register.html')
