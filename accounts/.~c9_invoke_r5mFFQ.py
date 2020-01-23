from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db import models
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm
from home.views import home_main
from recipes.models import Product
from recipes.views import all_products
from accounts.models import Profile
from accounts.forms import profile_form, user_form


# Create your views here.

def home_accounts(request):
    """Return the index.html file"""
    products = Product.objects.all()
    return render(request,  'index.html' , {"products": products})
    
    
@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('home_main'))



def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('home_accounts'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            messages.success(request, "You have successfully logged in!")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('home_main'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})
    
    
def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})
    
    
def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(username=request.user)
    user_email = user.email
    profile = get_object_or_404(Profile, pk=pk) if pk else None
    return render(request, 'profile.html', {"user": user, "user_email": user_email,
        'user_profile': user_profile
    })   



def edit_user_profile(request, pk=None):
    
    
    profile = get_object_or_404(Profile, pk=pk) if pk else None
    if request.method == "POST":
        user_profile_form = profile_form(request.POST, request.FILES, instance=profile)
        if user_profile_form.is_valid():
            profile = user_profile_form.save()
            return redirect(user_profile, profile.pk)
    else:
        user_profile_form = profile_form(instance=profile)
    return render(request, 'edit_user_profile.html', {
        'user_profile_form': user_profile_form,
    })
    
    
    

    
  
  
