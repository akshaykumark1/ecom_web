from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.signin, name='signin'),  # Ensure this line is here
    path('cart/', views.Cart_view, name='cart'),
    path('signup',views.signup,name='signup'),
    path('orders',views.orders,name='orders'),
    path('help',views.help,name='help'),
    path('log-out',views.userlogout,name='userlogout'),
    path('cart',views.Cart_view, name='cart'),


    path('adm',views.admin,name='admin'),

    # path('logout',views.slogout, name='logout'),
    # path('add_product',views.Add_product,name='add_product'),
    # path('selleradd',views.selleradd,name='selleradd'),
    # path('sellerview',views.sellerview,name='sellerview'),
    # path('edit_product/<int:id>/',views.edit_product, name='edit_product'),  
    # path('delete_view/<int:id>/',views.delete_view, name='delete_view'),   
 

 



    path('product_buy',views.product_buy,name='product_buy'),   
    path('wheretobuy',views.wheretobuy,name='wheretobuy'),
    path('buy-now', views.buy_now, name='buy_now'),
    # Change this line
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('product_details/<int:pk>/',views.product_detail, name='product_detail'),   
    path('account',views.account,name='account'),
    # path('product')







    
    path('address',views.address,name='address'),
    path('security',views.security,name='security'),

#____________________wishlist___________________________#
    path('wishlist',views.wishlist,name='wishlist'),
    path('addtowishlist/<int:product_id>/', views.addtowishlist, name='addtowishlist'),
    path('remove-from-wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),






    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
