from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('cart',views.cart,name='cart'),
    path('orders',views.orders,name='orders'),
    path('help',views.help,name='help'),
    path('log-out',views.userlogout,name='userlogout'),




    path('sellerhome',views.seller,name='seller'),
    path('seller',views.sellerin,name='sellerin'),
    path('registration',views.registration,name='registration'),
    path('logout',views.slogout, name='logout'),
    path('add_product',views.Add_product,name='add_product'),
    path('selleradd',views.selleradd,name='selleradd'),
    path('sellerview',views.sellerview,name='sellerview'),
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),  
    path('delete_view/<int:id>/', views.delete_view, name='delete_view'),   
    


    path('search',views.search,name='search'),
    path('cart_display',views.cart_display,name='cart_display'),
    path('delete_all',views.delete_all,name='delete_all'),








    path('product_buy',views.product_buy,name='product_buy'),   
    path('wheretobuy',views.wheretobuy,name='wheretobuy')


] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
