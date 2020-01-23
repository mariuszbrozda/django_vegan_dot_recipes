from django.conf.urls import url, include
from home.views import home_main


urlpatterns = [
    url(r'^home_main/', home_main, name="home_main"),

]