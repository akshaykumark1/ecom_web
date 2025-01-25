# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'base.html')
    
    
    
def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')    

def cart(request):
    return render(request, 'cart.html')    

def orders(request):
    return render(request, 'orders.html')  
def help(request):
    return render(request, 'help.html') 

@login_required(login_url='sellerin')
def seller(request):
    return render(request, 'seller/seller.html')    

def sellerin(request):
    if request.user.is_authenticated:
        return redirect('seller')
    username=None
    password=None 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            messages.error(request, 'Please fill in all fields.')
            return render(request, 'seller/sellerin.html')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['username'] = user.username
            request.session['user_id'] = user.id
            return redirect('seller')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'seller/sellerin.html')


def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_seller = True
            user.save()
            messages.success(request, 'Account created successfully.')

            return render('seller/sellerin.html')
    return render(request, 'seller/registration.html')


def logout(request):
    request.session.flush()
    return render(request, 'seller/sellerin.html')  # A custom template after logout


@login_required(login_url='sellerin')
def Add_product(request):
    return render(request, 'seller/selleradd.html')


def selleradd(request):
    return render(request, 'seller/selleradd.html')


