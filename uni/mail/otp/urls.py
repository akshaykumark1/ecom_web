from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('otp/', views.otp_view, name='otp'),  # OTP verification page
    path('', views.home, name='home'),  # Home page after login
]
