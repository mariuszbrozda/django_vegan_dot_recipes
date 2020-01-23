
from django.shortcuts import render, redirect, reverse
from home.views import home_main
from django.shortcuts import render, get_object_or_404, reverse, redirect
from cart.contexts import cart_contents
from recipes.models import Product
from checkout.forms import MakePaymentForm, OrderForm
from checkout.models import OrderLineItem



# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    
    return render(request, "cart.html" )


    
    


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = 1
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = 1
    
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('home_main'))
    
    
    

def delete_recipe_from_cart(request, id):
    quantity = 1
    product = get_object_or_404(Product, pk=id)
    
    cart = request.session.get('cart', {})
    
    cart_items = []
    
    if id in cart:
        cart[id] = int(cart[id]) - quantity  
        cart.pop(id)
    else:
        cart[id] = cart.get(id, quantity) 
  
    request.session['cart'] = cart
    
    return redirect(reverse('view_cart') )
    

def delete_recipe_from_checkout(request, id):
    quantity = 1
    product = get_object_or_404(Product, pk=id)
    
    cart = request.session.get('cart', {})
    
    cart_items = []
    
    if id in cart:
        cart[id] = int(cart[id]) - quantity  
        cart.pop(id)
    else:
        cart[id] = cart.get(id, quantity) 
  
    request.session['cart'] = cart
    
    return redirect(reverse('checkout'))