from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout


User = get_user_model()


def register_view(request):
    if request.method == 'GET':
        return render(request, 'auth/register.html')
    
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')
        
        user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, password=password)
        user.save()

        messages.success(request, 'Account created successfully')
        return redirect('login')
    

def login_view(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('/')

def profile_view(request):
    return render(request, 'auth/profile.html')