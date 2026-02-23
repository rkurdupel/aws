from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse


def home(request):
    user_role = ''
    if request.user.is_authenticated:
        if request.user.role == 0:
            user_role = 'visitor'
        elif request.user.role == 1:
            user_role = 'librarian'

    context = {'user_role': user_role}
    return render(request, 'authentication/home.html', context)


def register(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        context['form'] = form

        if form.is_valid():
            first_name = request.POST.get('first_name')
            middle_name = request.POST.get('middle_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            role = request.POST.get('role')
            

            if role == '1':
                user = CustomUser.objects.create_superuser(
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                )
            else:
                user = CustomUser.objects.create_user(
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                )

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'authentication/registration.html', {'error_message': 'Registration failed'})
    else:
        form = RegisterForm()
        context['form'] = form
    return render(request, 'authentication/registration.html', context)


def loginPage(request):
  
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        context['form'] = form
        
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)  
            
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('<h1>Email address or password is incorrect</h1>')
        
       
    else:
        form = LoginForm()
        context['form'] = form
   # context = {'page': page}
    return render(request, 'authentication/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')
