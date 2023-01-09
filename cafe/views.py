from django.shortcuts import render,redirect
from .models import Coffee
from django.contrib import messages
from .models import * 
from django import template

register=template.Library()
# Create your views here.
def home(request):
    return render(request,'home.html')
def menu(request):
    return render(request,'menu.html')
def coffee(request):
    coffees=Coffee.objects.all()
    ctx={'coffees':coffees}
    #print("We are in coffee")
    coffee=request.POST.get('coffee')
    cart=request.session.get('cart')
    #print(cart)
    if cart:
        quantity=cart.get(coffee)
        print(quantity)
        if quantity :
            cart[coffee]=quantity+1
        else:
            cart[coffee]=1
    else:
        cart={}
        cart[coffee]=1
    if 'null' in cart:
        del cart['null']
    
    request.session['cart']=cart
    return render(request,'coffee.html',ctx)


def aboutus(request):
    return render(request,'aboutus.html')

@register.filter(name='cart_quantity')
def cart_quantity(coffee,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==coffee.id:
            return cart.get(id)
    return 0

@register.filter(name='price_total')
def price_total(coffee,cart):
    return coffee.price*cart_quantity(coffee,cart)


@register.filter(name='total_cart_price')
def total_cart_price(coffee,cart):
    sum=0
    for p in coffee:
        sum=sum+price_total(p,cart)
    return sum
def remove_quantity(request):
    coffees=Coffee.objects.all()
    ctx={'coffees':coffees}
    #print("We are in coffee")
    coffee=request.POST.get('remove')
    print(coffee)
    cart=request.session.get('cart')
    
    if cart:
        quantity=cart.get(coffee)
        print(quantity)
        if quantity>1 :
            cart[coffee]=quantity-1
        elif quantity==1:
             del cart[coffee]
    else:
        cart={}
        cart[coffee]=1
    if 'null' in cart:
        del cart['null']
    request.session['cart']=cart
    print(cart)

def add_quantity(request):
    coffees=Coffee.objects.all()
    ctx={'coffees':coffees}
    #print("We are in coffee")
    coffee=request.POST.get('add')
    cart=request.session.get('cart')
    #print(cart)
    if cart:
        quantity=cart.get(coffee)
        print(quantity)
        if quantity :
            cart[coffee]=quantity+1
        else:
            cart[coffee]=1
    else:
        cart={}
        cart[coffee]=1
    if 'null' in cart:
        del cart['null']
    request.session['cart']=cart


def cart(request):
    remove=request.POST.get('remove')
    #print("Remove:",remove)
    add=request.POST.get('add')
    print("Add:",add)
    if remove:
        remove_quantity(request)
    if add:
        add_quantity(request)

    ids = list(request.session.get('cart').keys())
    coffee = Coffee.get_products_by_id(ids)
    cart=request.session.get('cart')
    quantity=[]
    for c in coffee:
        quantity.append(cart_quantity(c,cart))
    total=total_cart_price(coffee,cart)
    myzip=zip(coffee,quantity)
    ctx={'myzip':myzip,'total':total}
    return render(request,'cart.html',ctx)

def check(request):
    address=request.POST.get('address')
    phone=request.POST.get('phone')
    print(address,phone)
    return  redirect('cart.html')

