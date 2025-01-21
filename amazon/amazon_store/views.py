# myapp/views.py
from django.shortcuts import render

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