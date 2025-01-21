from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
  path('home',views.home,name='home'),
  path('',views.signin,name='signin'),
  path('signup',views.signup,name='signup'),
  path ('otp',views.otp_view,name='otp'),
]