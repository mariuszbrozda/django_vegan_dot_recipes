from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart
from cart.views import delete_recipe_from_cart, delete_recipe_from_checkout
from cart.contexts import cart_contents

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
    url(r'^remove/(?P<id>\d+)', delete_recipe_from_cart, name='delete_recipe_from_cart'),
    url(r'^(?P<id>\d+)', delete_recipe_from_checkout, name='delete_recipe_from_checkout')
]