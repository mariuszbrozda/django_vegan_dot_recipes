from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db import models
from urllib import request
from recipes.forms import Add_recipe_form
from django.contrib import auth, messages
from recipes.models import Product
from cart.views import view_cart
from home.views import home_main
from django.conf import settings
from django.contrib.auth.models import User
from .contexts import purchased_contents
from checkout.models import Purchases

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})



## ------------------STARTER -----


# Function for 'STARTERS' that gets username var from session
# and finds all STARTERS recipes in MongoDB recipes collection
def starters(request):
    starters_recipes = Product.objects.filter(recipe_category_name="Starters")
    return render(request, "starters.html", { 'starters_recipes': starters_recipes})
    

## ------------------MAIN COURSE -----    

def main_courses(request):
    main_courses_recipes = Product.objects.filter(recipe_category_name="Main courses")
    return render(request, "main_courses.html", { 'main_courses_recipes': main_courses_recipes})
# Function for 'Main courses' that gets username var from session
# and finds all Main courses recipes in MongoDB recipes collection


## ------------------DESERS -----    

# Function for 'Desers' that gets username var from session
# and finds all Desers recipes in MongoDB recipes collection
def desers(request):
    desers_recipes = Product.objects.filter(recipe_category_name="Desers")
    return render(request, "desers.html", { 'desers_recipes': desers_recipes})
    
    
## ------------------SMOOTHIES ROUTES -----

# Function for 'Smoothies' that gets username var from session
# and finds all Smoothies recipes in MongoDB recipes collection
def smoothies(request):
    smoothies_recipes = Product.objects.filter(recipe_category_name="Smoothies")
    return render(request, "smoothies.html", { 'smoothies_recipes': smoothies_recipes})
    
    

## ------------------JUICES ROUTES -----   

# Function for 'Juices' that gets username var from session
# and finds all Juices recipes in MongoDB recipes collection
def juices(request):
    juices_recipes = Product.objects.filter(recipe_category_name="Juices")
    return render(request, "juices.html", { 'juices_recipes': juices_recipes})



def recipe_detail(request, pk):
    recipe = get_object_or_404(Product, pk=pk)
    recipe.views += 1
    recipe.save()
    return render(request, "recipe_details.html", {'recipe': recipe})


## ----------------------------------------------ADD RECIPE ROUTE ----- 

# Function for adding recipe that gets username var from session
# and finds all recipe's categories and return add_recipe page


def add_recipe(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    
    recipe = get_object_or_404(Product, pk=pk) if pk else None
    if request.method == "POST":
        add_recipe_form = Add_recipe_form(request.POST, request.FILES)
        
        if add_recipe_form.is_valid():
            recipe = add_recipe_form.save()
            return redirect(recipe_detail, recipe.pk)
    else:
        add_recipe_form = Add_recipe_form()
        
    return render(request, 'add_recipe.html', {'add_recipe_form': add_recipe_form,})
 
    

def edit_recipe(request, id):
    product_to_edit = get_object_or_404(Product, pk=id)
    add_recipe_form = Add_recipe_form(request.POST, request.FILES)
    if request.method == "POST":
        add_recipe_form = Add_recipe_form(request.POST, request.FILES, instance=product_to_edit)
        
        if add_recipe_form.is_valid():
            
            add_recipe_form.save()
            return redirect(recipe_detail)
    else:
        add_recipe_form = Add_recipe_form(instance=product_to_edit)
        
    return render(request, 'add_recipe.html', {'add_recipe_form': add_recipe_form, 'product': product_to_edit})

    
def delete_recipe(request, pk):
    recipe = get_object_or_404(Product, pk=pk)
    recipe.delete()
    return redirect(reverse('user_profile'))


def delete_recipe_from_purchases(request, pk):
    recipe = get_object_or_404(Purchases, pk=pk)
    recipe.delete()
    return redirect(reverse('user_profile'))





