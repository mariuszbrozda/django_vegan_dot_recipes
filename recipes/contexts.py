from django.shortcuts import get_object_or_404
from recipes.models import Product


def purchased_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    purchased_recipes = request.session.get('purchased_recipes', {})

    purchased_items = []
    total = 0
    product_count = 0
    
    for id, quantity in purchased_recipes.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        purchased_items += quantity
        purchased_items.append({'id': id, 'quantity': quantity, 'product': product})
    
    return {'purchased_items': purchased_items, 'total': total, 'product_count': product_count}