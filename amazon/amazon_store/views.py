# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


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


def seller(request):

    return render(request, 'seller.html')    
def sellerin(request):
    if request.user.is_authenticated:
        return redirect('seller')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            messages.error(request, 'Please fill in all fields.')
            return render(request, 'sellerin.html')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['username'] = user.username
            return redirect('seller')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'sellerin.html')


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
            user.save()
            return redirect('signin')

    return render(request, 'registration.html')

