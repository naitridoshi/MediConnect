from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from .form import *

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


@login_required(login_url="/login/")
def user(request):
    blogs = BlogModel.objects.filter(draft=False)
    context = {'blogs': blogs}

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
            return redirect('/blogs')
    else:
        return render(request, 'login_page.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url="/login/")
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required(login_url="/login/")
def add_blog(request):
    context = {'form': BlogForm}

    if request.method == 'POST':
        form = BlogForm(request.POST)
        image = request.FILES.get('image')
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        category = request.POST.get('gridRadios')
        user = request.user
        draft = request.POST.get('isDraft')

        if form.is_valid():
            print('Valid')
            content = form.cleaned_data['content']

        if draft == 'Valid':
            draft = True
        else:
            draft = False

        data = BlogModel.objects.create(
            user=user,
            content=content,
            title=title,
            image=image,
            summary=summary,
            category=category,
            draft=draft
        )
        return redirect('/my-blogs')
    return render(request, 'add_blog.html', context)


@login_required(login_url="/login/")
def blog_detail(request, slug):
    context = {}
    blog_obj = BlogModel.objects.filter(slug=slug).first()
    context['blog_obj'] = blog_obj
    return render(request, 'blog_detail.html', context)


@login_required(login_url="/login/")
def myblogs(request):
    context = {}
    blog_objs = BlogModel.objects.filter(user=request.user)
    context['blog_objs'] = blog_objs
    return render(request, 'myblogs.html', context)


@login_required(login_url="/login/")
def blog_delete(request, id):
    blog_obj = BlogModel.objects.get(id=id)
    if blog_obj.user == request.user:
        blog_obj.delete()
    return redirect('/my-blogs/')


@login_required(login_url="/login/")
def blog_update(request, slug):
    context = {}
    blog_obj = BlogModel.objects.get(slug=slug)
    if blog_obj.user != request.user:
        return redirect('/my-blogs')

    initial_dict = {'content': blog_obj.content}
    form = BlogForm(initial=initial_dict)
    context['blog_obj'] = blog_obj
    context['form'] = form
    if request.method == 'POST':
        form = BlogForm(request.POST)
        # print(request.FILES)
        image = request.FILES.get('image')
        title = request.POST.get('title')
        user = request.user
        category = request.POST.get('gridRadios')
        summary = request.POST.get('summary')
        draft = request.POST.get('isDraft')
        print(draft)

        if form.is_valid():
            content = form.cleaned_data['content']
            form.save()

        if draft == 'Valid':
            draft = True
        else:
            draft = False

        obj = BlogModel.objects.get(slug=slug)
        obj.user = user
        obj.title = title
        obj.category = category
        obj.summary = summary
        obj.image = image
        obj.draft = draft
        obj.save()
        # blog_obj = BlogModel.objects.create(
        #     user=user, title=title,
        #     content=content, image=image,
        #     summary=summary, category=category,
        #     draft=draft
        # )

    return render(request, 'update_blog.html', context)


def mental_health(request):
    blogs = BlogModel.objects.filter(category='Mental Health')
    context = {'blogs': blogs}
    return render(request, 'mental_health.html', context)


def heart_disease(request):
    blogs = BlogModel.objects.filter(category='Heart Disease')
    context = {'blogs': blogs}
    return render(request, 'mental_health.html', context)


def covid19(request):
    blogs = BlogModel.objects.filter(category='Covid 19')
    context = {'blogs': blogs}
    return render(request, 'mental_health.html', context)


def immunization(request):
    blogs = BlogModel.objects.filter(category='Immunization')
    context = {'blogs': blogs}
    return render(request, 'mental_health.html', context)
