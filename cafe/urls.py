from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('menu.html',views.menu,name="menu"),
    path('coffee.html',views.coffee,name="coffee"),
    path('cart.html',views.cart,name="cart"),
    #path('remove',views.remove,name="remove")
]