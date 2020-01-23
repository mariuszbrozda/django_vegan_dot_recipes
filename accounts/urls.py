from django.conf.urls import url, include
from accounts.views import home_accounts, logout, login, registration, user_profile
from recipes.views import all_products, recipe_detail
from accounts import url_reset
from home.views import home_main
from recipes import urls as urls_recipes

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^password-reset/', include(url_reset)),
    
    url(r'^user_profile/', user_profile, name="user_profile"),
  
    
    url(r'^recipe_detail/', recipe_detail, name='recipe_detail'),
    
    
    url(r'^home_main/', home_main, name="home_main"),
]