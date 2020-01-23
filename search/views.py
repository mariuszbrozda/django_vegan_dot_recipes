from django.shortcuts import render
from recipes.models import Product

# Create your views here.
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "home.html", {"products": products})