from django.shortcuts import render, redirect
from .models import Coffee
from django.contrib import messages
from .models import *
from django import template

register = template.Library()
# Create your views here.


def home(request):
    return render(request, 'home.html')


def menu(request):
    return render(request, 'menu.html')


def coffee(request):
    coffees = Coffee.objects.all()
    ctx = {'coffees': coffees}
    # print("We are in coffee")
    coffee = request.POST.get('coffee')
    cart = request.session.get('cart')
    # print(cart)
    if cart:
        quantity = cart.get(coffee)
        print(quantity)
        if quantity:
            cart[coffee] = quantity+1
        else:
            cart[coffee] = 1
    else:
        cart = {}
        cart[coffee] = 1
    if 'null' in cart:
        del cart['null']

    request.session['cart'] = cart
    return render(request, 'coffee.html', ctx)


def aboutus(request):
    return render(request, 'aboutus.html')


@register.filter(name='cart_quantity')
def cart_quantity(coffee, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == coffee.id:
            return cart.get(id)
    return 0


@register.filter(name='price_total')
def price_total(coffee, cart):
    return coffee.price*cart_quantity(coffee, cart)


@register.filter(name='total_cart_price')
def total_cart_price(coffee, cart):
    sum = 0
    for p in coffee:
        sum = sum+price_total(p, cart)
    return sum


def remove_quantity(request):
    coffees = Coffee.objects.all()
    ctx = {'coffees': coffees}
    # print("We are in coffee")
    coffee = request.POST.get('remove')
    print(coffee)
    cart = request.session.get('cart')

    if cart:
        quantity = cart.get(coffee)
        print(quantity)
        if quantity > 1:
            cart[coffee] = quantity-1
        elif quantity == 1:
             del cart[coffee]
    else:
        cart = {}
        cart[coffee] = 1
    if 'null' in cart:
        del cart['null']
    request.session['cart'] = cart
    print(cart)


def add_quantity(request):
    coffees = Coffee.objects.all()
    ctx = {'coffees': coffees}
    # print("We are in coffee")
    coffee = request.POST.get('add')
    cart = request.session.get('cart')
    # print(cart)
    if cart:
        quantity = cart.get(coffee)
        print(quantity)
        if quantity:
            cart[coffee] = quantity+1
        else:
            cart[coffee] = 1
    else:
        cart = {}
        cart[coffee] = 1
    if 'null' in cart:
        del cart['null']
    request.session['cart'] = cart


def cart(request):
    remove = request.POST.get('remove')
    # print("Remove:",remove)
    add = request.POST.get('add')
    # print("Add:",add)
    if remove:
        remove_quantity(request)
    if add:
        add_quantity(request)

    ids = list(request.session.get('cart').keys())
    if 'null' in ids:
        ids.remove('null')
    coffee = Coffee.get_products_by_id(ids)
    cart = request.session.get('cart')
    quantity = []
    for c in coffee:
        quantity.append(cart_quantity(c, cart))
    total = total_cart_price(coffee, cart)
    myzip = zip(coffee, quantity)
    ctx = {'myzip': myzip, 'total': total}
    
    return render(request, 'cart.html', ctx)
    



def check(request):
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    cart = request.session.get('cart')
    coffees = Coffee.get_products_by_id(list(cart.keys()))
    for coffee in coffees:
        order = Order(product=coffee, quantity=(cart.get(str(coffee.id))),
                      price=coffee.price, address=address, phone=phone)
        order.save()
    request.session['cart'] = {}

    print(address, phone)
    return redirect('cart.html')


def order(request):
    order = Order.objects.all()
    print(order)
    return render(request, 'order.html', {'orders': order})


def login(request):

    return render(request, 'login.html')


def validateCustomer(customer):
    error_message = None
    if (not customer.first_name):
        error_message = "First Name Required !!"
    elif len(customer.first_name) < 4:
        error_message = 'First Name must be 4 char long or more'
    elif not customer.last_name:
        error_message = 'Last Name Required'
    elif len(customer.last_name) < 4:
        error_message = 'Last Name must be 4 char long or more'
    elif not customer.phone:
        error_message = 'Phone Number required'
    elif len(customer.phone) < 10:
        error_message = 'Phone Number must be 10 char Long'
    elif len(customer.password) < 6:
        error_message = 'Password must be 6 char long'
    elif len(customer.email) < 5:
        error_message = 'Email must be 5 char long'
    elif customer.isExists():
        error_message = 'Email Address Already Registered..'
        # saving

    return error_message
def signup(request):
    return render(request,'signup.html')


def sign(request):
    first_name = request.POST.get('firstname')
    last_name = request.POST.get('lastname')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    password = request.POST.get('password')
    customer = Customer(first_name=first_name, last_name=last_name,
                    phone=phone, email=email, password=password)

    value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
    error_message = validateCustomer(customer)
    if not error_message:
            # customer.password = make_password(customer.password)
        customer.register()
        return redirect('order.html')
    else:
        data = {
                'error': error_message,
                'values': value
            }
    return render(request, 'signup.html', data)
    #return render(request,'signup.html')


        

