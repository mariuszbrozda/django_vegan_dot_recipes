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

# Function to get all recipes list
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})



## ------------------STARTER -----


# Function for 'STARTERS'
#finds all STARTERS recipes in DB recipes based on filter
def starters(request):
    starters_recipes = Product.objects.filter(recipe_category_name="Starters")
    return render(request, "starters.html", { 'starters_recipes': starters_recipes})
 
 
    
## ------------------MAIN COURSES -----   

# Function for 'Main courses'
#finds all Main courses recipes in DB recipes based on filter   

def main_courses(request):
    main_courses_recipes = Product.objects.filter(recipe_category_name="Main courses")
    return render(request, "main_courses.html", { 'main_courses_recipes': main_courses_recipes})
    
    

## ------------------DESERS -----    

# Function for 'Desers'
# and finds all Desers recipes in DB recipes based on filter
def desers(request):
    desers_recipes = Product.objects.filter(recipe_category_name="Desers")
    return render(request, "desers.html", { 'desers_recipes': desers_recipes})
    
    
## ------------------SMOOTHIES -----

# Function for 'Smoothies'
# and finds all Smoothies recipes in DB recipes based on filter
def smoothies(request):
    smoothies_recipes = Product.objects.filter(recipe_category_name="Smoothies")
    return render(request, "smoothies.html", { 'smoothies_recipes': smoothies_recipes})
    
    

## ------------------JUICES -----   

# Function for 'Juices' 
# and finds all Juices recipes in DB recipes based on filter

def juices(request):
    juices_recipes = Product.objects.filter(recipe_category_name="Juices")
    return render(request, "juices.html", { 'juices_recipes': juices_recipes})


# and finds all Juices recipes in DB recipes based on filter
def recipe_detail(request, pk):
    recipe = get_object_or_404(Product, pk=pk) 
    recipe.views += 1
    recipe.save()
    return render(request, "recipe_details.html", {'recipe': recipe})




## ----------------------------------------------ADD RECIPE ----- 

# Function for adding recipe to database based on recipe model
# Return add_recipe page


def add_recipe(request, pk=None):
    
    recipe = get_object_or_404(Product, pk=pk) if pk else None
    if request.method == "POST":
        add_recipe_form = Add_recipe_form(request.POST, request.FILES)
        
        if add_recipe_form.is_valid():
            recipe = add_recipe_form.save()
            return redirect(recipe_detail, recipe.pk)
    else:
        add_recipe_form = Add_recipe_form()
        
    return render(request, 'add_recipe.html', {'add_recipe_form': add_recipe_form,})
 
 
## ----------------------------------------------EDIT RECIPE ----- 

# Function for edit particular recipe and update in database based on recipe model
# Return add_recipe page  

def edit_recipe(request, id):
    product_to_edit = get_object_or_404(Product, pk=id)
    add_recipe_form = Add_recipe_form(request.POST, request.FILES)
    if request.method == "POST":
        add_recipe_form = Add_recipe_form(request.POST, request.FILES, instance=product_to_edit)
        
        if add_recipe_form.is_valid():
            
            add_recipe_form.save()
            return redirect(recipe_detail, pk=id)
    else:
        add_recipe_form = Add_recipe_form(instance=product_to_edit)
        
    return render(request, 'add_recipe.html', {'add_recipe_form': add_recipe_form, 'product': product_to_edit})


## -----------------------DELETE RECIPE FROM WEBSITE AND SECTION UPLOADED BY ME----- 

# Function for delete recipe from database. recipe is localise by primary key
# Return user_profile view
    
def delete_recipe(request, pk):
    recipe = get_object_or_404(Product, pk=pk)
    recipe.delete()
    return redirect(reverse('user_profile'))



## ---------------DELETE RECIPE FROM SECTION PURCHASED BY ME----- 

# Function for delete recipe from database. recipe is localise by primary key and
# deleted from DB based on purchasess model
# Return user_profile view
def delete_recipe_from_purchases(request, pk):
    recipe = get_object_or_404(Purchases, pk=pk)
    recipe.delete()
    return redirect(reverse('user_profile'))





