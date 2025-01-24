from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('cart',views.cart,name='cart'),
    path('orders',views.orders,name='orders'),
    path('help',views.help,name='help'),
    path('seller',views.seller,name='seller'),
    path('sellerin',views.sellerin,name='sellerin'),
    path('registration',views.registration,name='registration'),

]
