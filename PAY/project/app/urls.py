from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('order_ payment',views.order_payment,name='order_payment')

    

]
