# myapp/views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

def home(request):
    return render(request, 'base.html')
    
    
    
def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    username=None
    password=None 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            messages.error(request, 'Please fill in all fields.')
            return render(request, 'signin.html')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['username'] = user.username
            request.session['user_id'] = user.id
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'signin.html')

def signup(request):
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

            return render(request,'signin.html')
    return render(request, 'signup.html')





def userlogout(request):
    logout(request)
    return redirect('signin')  # A custom template after logout






def cart(request):
    return render(request, 'cart.html')    

def orders(request):
    return render(request, 'orders.html')  
def help(request):
    return render(request, 'help.html') 



def protien(request):
    products = Product.objects.all()

    return render(request, 'protien.html', {'products': products})

def creatine(request):
    products = Product.objects.all()

    return render(request, 'creatine.html', {'products': products})


def  preworkout(request):
    products = Product.objects.all()

    return render(request, 'prework.html', {'products': products})














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

            return render(request,'seller/sellerin.html')
    return render(request, 'seller/registration.html')


def slogout(request):
    request.session.flush()
    return render(request, 'seller/sellerin.html')  # A custom template after logout


@login_required(login_url='sellerin')
def Add_product(request):
    return render(request, 'seller/selleradd.html')


def selleradd(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        description = request.POST.get('description')

        # Check if all required fields are provided
        if not title or not price or not category or not image or not description:
            messages.error(request, "All fields are required!")
            return render(request, 'seller/selleradd.html')

        # Create and save product object
        product = Product(
            title=title,
            price=price,
            category=category,
            image=image,
            description=description
        )
        product.save()

        # Success message
        messages.success(request, "Product added successfully!")
        return redirect('sellerview')
    
    # If GET request, render the page with empty form
    return render(request, 'seller/selleradd.html')


def sellerview(request):
    products = Product.objects.all()
    
    return render(request, 'seller/seller.html', {'products': products})



def edit_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        description = request.POST.get('description')


        # Check if all required fields are provided
        if not title or not price or not category or not description:
            messages.error(request, "All fields are required!")
            return render(request, 'seller/edit.html', {'product': product})

        # Update and save product object
        product.title = title
        product.price = price
        product.category = category
        if image:
            product.image = image
        product.description = description
        product.save()

        # Success message
        messages.success(request, "Product updated successfully!")
        return render(request, 'seller/seller.html')
    
    # If GET request, render the page with empty form
    return render(request, 'seller/edit.html', {'product': product})

def delete_view(request, id):
    product = Product.objects.filter(pk=id).first()  # Get product by ID (or None if not found)
    if product:
        product.delete()  # Delete the product
        messages.success(request, "Product deleted successfully!")  # Optional success message
    return redirect('sellerview')
