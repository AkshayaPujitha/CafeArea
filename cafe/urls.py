from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('menu.html',views.menu,name="menu"),
    path('coffee.html',views.coffee,name="coffee"),
    path('cart.html',views.cart,name="cart"),
    path('aboutus.html',views.aboutus,name="aboutus"),
    path('home.html',views.home,name="home"),
    path('check-out',views.check,name="check"),
    path('order.html',views.order,name="order"),
    path('login.html',views.login,name="login"),
    path('signup.html',views.signup,name="signup"),
    path('signup',views.sign,name="sign"),
]