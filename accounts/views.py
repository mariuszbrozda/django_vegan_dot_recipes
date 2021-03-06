from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db import models
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm
from home.views import home_main
from recipes.models import Product
from recipes.views import all_products
from accounts.models import Profile
from accounts.forms import profile_form
from checkout.models import OrderLineItem, Purchases

# Create your views here.

def home_accounts(request):
    """Return the index.html file"""
    products = Product.objects.all()
    return render(request,  'index.html' , {"products": products})
    
    
## ---------------LOG OUT ----- 

# Function for logout user from website
# after that user will see seucces message
    
@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('home_main'))

## ---------------LOG in ----- 

# Function for login user to website
# after that user will see seucces message

def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('home_main'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('home_main'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})
## ---------------registration ----- 

# Function for registration and create user account with password username and email
# after that user will see seucces messag   

def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('home_main'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('home_main'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})


## ---------------User Profile view ----- 

# Function for user profile, presents user account with  username and email
# added and purchased recipes
    
def user_profile(request, pk=None):
    """The user's profile page"""
    recipe = get_object_or_404(Product, pk=pk) if pk else None
    
    user = User.objects.get(username=request.user)
    user_email = user.email
    uploaded_by_me = Product.objects.filter(uploaded_by=user)
   
    purchased = Purchases.objects.filter(user=user)
    
    return render(request, 'profile.html', {"user": user, "user_email": user_email,
                 'uploaded_by_me':uploaded_by_me, 'purchased': purchased, 
                
                 })   
    
    

    
  
  
