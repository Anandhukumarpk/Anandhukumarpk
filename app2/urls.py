from django.urls import path
from . import views
from cart.views import cart


urlpatterns = [

    path('orderplace/',views.orderplace , name='orderplace'),
    path('orders/', views.orderpage , name='orderpage'),
    path('confirmOrder/', views.confirmOrder , name='confirmOrder'),
    path('payment/', views.payment , name='payment'),
    path('orderpage', views.orderpage , name='orderpage'),
    path('cart',views.cart, name='cart'),
    path('contact', views.contact , name='contact'),
    path('faq', views.faq , name='faq'),

    
    
   
   

    

]