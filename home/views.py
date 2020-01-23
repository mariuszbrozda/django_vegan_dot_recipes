
from recipes.models import Product
from django.shortcuts import render, redirect, reverse, get_object_or_404


# Create your views here.
def home_main(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})