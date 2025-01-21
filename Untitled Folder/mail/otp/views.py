from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import pyotp
from datetime import datetime, timedelta

def home(request):
    return render(request, 'home.html')
def signin(request):
    # If the user is already authenticated, redirect to the home page.
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to 'home' view by its URL name.
    
    # Handle POST request when the user submits the login form.
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if both fields are filled in.
        if not username or not password:
            messages.error(request, 'Please enter both username and password.')
            return render(request, 'signin.html')  # Ensure the template is returned
        
        # Authenticate the user.
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Send OTP after successful authentication.
            send_otp(request, user)  # Send OTP function
            request.session['username'] = user.username
            request.session['email'] = user.email
            
            # Redirect to OTP verification page
            return redirect('otp')  # Redirect to OTP verification view
        else:
            messages.error(request, 'Invalid username or password.')
    
    # Handle GET request (just render the sign-in page).
    return render(request, 'signin.html')




def signup(request):
    # Handle GET request (show the signup form).
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    # Handle POST request (form submission).
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        
        # Check if passwords match.
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')
        
        # Check if email already exists.
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'signup.html')
        
        # Check if username already exists.
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'signup.html')
        
        # Create the new user.
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Account created successfully.')
        
        # Redirect to the signin page after successful signup.
        return redirect('signin')  # Make sure 'signin' matches the URL name of the sign-in page.


def send_otp(request, user):
    totp = pyotp.TOTP(pyotp.random_base32(), interval=30)
    otp = totp.now()
    request.session['otp_key'] = totp.secret  # Store OTP secret key in session
    valid = datetime.now() + timedelta(minutes=1)
    request.session['otp_date'] = valid.isoformat()  # Store OTP expiration time in session

    email = user.email
    if email:
        try:
            send_mail(
                subject='OTP Verification',
                message=f'Your OTP is {otp}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            print(f"OTP sent to {email}")
        except BadHeaderError:
            print(f"Error sending OTP to {email}")
    else:
        print("Email not found")

def otp_view(request):
    error_message = None
    if request.method == 'POST':
        otp = request.POST.get('otp')
        username = request.POST.get('username')
        otp_key = request.session.get('otp_key')
        otp_date = request.session.get('otp_date')

        if otp_key and otp_date:
            valid = datetime.fromisoformat(otp_date)
            if valid > datetime.now():  # Check if OTP has expired
                totp = pyotp.TOTP(otp_key, interval=60)
                if totp.verify(otp):  # Verify the OTP
                    user = get_object_or_404(User, username=username)
                    login(request, user)
                    del request.session['otp_key']  # Remove OTP key from session
                    del request.session['otp_date']  # Remove OTP expiration date from session
                    return redirect('home')  # Redirect to home page after successful login
                else:
                    error_message = 'Invalid OTP'
            else:
                error_message = 'OTP expired'
        else:
            error_message = 'OTP not found'

    return render(request, 'otp.html', {'error': error_message})
