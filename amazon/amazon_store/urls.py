from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('cart',views.cart,name='cart'),
    path('orders',views.orders,name='orders'),
    path('help',views.help,name='help'),
    path('sellerhome',views.seller,name='seller'),
    path('seller',views.sellerin,name='sellerin'),
    path('registration',views.registration,name='registration'),
    path('logout',views.logout, name='logout'),
    path('add_product',views.Add_product,name='add_product'),
    path('selleradd',views.selleradd,name='selleradd'),
    path('sellerview',views.sellerview,name='sellerview'),
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),     
    path('delete_product/<int:id>/',views.delete_product,name='delete_product'),
    

]
