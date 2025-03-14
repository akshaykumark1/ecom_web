# myapp/views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

def home(request):
    product=Product.objects.all()

    return render(request, 'base.html',{'product':product})
    
    
    
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
            if user.is_superuser:
                return redirect('seller')
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



def cart(request):
    return render(request, 'user/cart.html')

def userlogout(request):
    logout(request)
    return redirect('signin')  # A custom template after logout
















def orders(request):
    return render(request, 'user/orders.html')  
def help(request):
    return render(request, 'user/help.html') 



def product_buy(request):
    products = Product.objects.all()

    return render(request, 'user/product_buy.html', {'products': products})

def wheretobuy(request):
    return render(request,'user/wheretobuy.html')

def buy_now(request):
    return render(request,'buy_now.html')





def process_payment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Add payment logic here (e.g., integrate with Stripe, PayPal, etc.)
    return render(request, 'payment_success.html', {'product': product})





def product_detail(request,pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'user/product_detail.html', {'product': product})



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
    return render(request, 'base.html')  # A custom template after logout


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



# def search(request):
#     if request.method == 'POST':
#         searched = request.POST.get('searched', '').strip()  # Get the search term
#         category = request.POST.get('category', '')  # Get the selected category (if any)
        
#         # Filter products based on the search term and category
#         results = Product.objects.all()
        
#         if searched:
#             results = results.filter(name__icontains=searched)
        
#         if category:
#             # Dynamically filter based on the category field
#             category_filter = {f"{category}": True}
#             results = results.filter(**category_filter)

#         return render(request, 'user/search.html', {'searched': searched, 'category': category, 'results': results})
    
#     # Render the empty search page for GET requests
#     return render(request, 'user/search.html', {'searched': '', 'category': '', 'results': []})



def delete_all(request):
    cart.objects.filter(user=request.user).delete()
    request.session['cart_cleared'] = True
    return redirect(cart)




def account(request):
    return render(request, 'accounts/account.html')

def address(request):
    return render(request,'accounts/address.html')

def security(request):
    return render(request,'accounts/security.html')

def product_display(request):
    products = Product.objects.all()
    
    return render(request, 'user/product_buy.html', {'products': products})

