from django.conf.urls import url, include
from recipes.views import all_products, delete_recipe_from_purchases, edit_recipe,  starters, main_courses, desers, juices,smoothies, recipe_detail, add_recipe, delete_recipe



urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^add/$', add_recipe, name='add_recipe'),
    url(r'^starters', starters, name='starters'),
    url(r'^main_courses', main_courses, name='main_courses'),
    url(r'^desers', desers, name='desers'),
    url(r'^smoothies', smoothies, name='smoothies'),
    url(r'^juices', juices, name='juices'),
    
    url(r'^(?P<id>\d+)/edit/$', edit_recipe, name='edit_recipe'),
    
    url(r'^(?P<pk>\d+)', recipe_detail, name='recipe_detail'),
    url(r'^delete_recipe(?P<pk>\d+)', delete_recipe, name='delete_recipe'),
    url(r'^(?P<pk>\d+)', delete_recipe_from_purchases, name='delete_recipe_from_purchases'),
]