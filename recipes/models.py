from django.db import models
from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth.models import User

from django.contrib import admin
from accounts.models import Profile
from django.shortcuts import render, redirect, reverse, get_object_or_404



# Create your models here.
class Product(models.Model):
    
    category_name = (
        ('Starters', 'Starters'),
        ('Main courses','Main courses'),
        ('Desers','Desers'),
        ('Smoothies','Smoothies'),
        ('Juices','Juices'),
    )
    
    
    recipe_category_name = models.CharField( max_length=20, choices=category_name, default='')
    views = models.IntegerField(default=0)
    uploaded_by =  models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=54, default='')
    description = models.TextField(max_length=148, default='')
    price = models.DecimalField( max_digits=6, decimal_places=2,)
    image = models.ImageField(upload_to='images', blank=True)
    
    recipe_name = models.CharField(max_length=254 , default='')
    cousine = models.CharField(max_length=25, default='' )
    
    preparation_time = models.CharField(max_length=25, default='')
    recipe_how_to_serve = models.CharField(max_length=354, default='')
    preparation_method_1 = models.TextField(max_length=300, default='')
    preparation_method_2 = models.TextField(max_length=300,blank=True, default='')
    preparation_method_3 = models.TextField(max_length=300,blank=True, default='')
    preparation_method_4 = models.TextField(max_length=300,blank=True, default='')
    preparation_method_5 = models.TextField(max_length=300,blank=True, default='')
    
    ingredient_1 = models.CharField(max_length=54, default='', blank=True)
    ingredient_2 = models.CharField(max_length=54, default='', blank=True)
    ingredient_3 = models.CharField(max_length=54, default='', blank=True)
    ingredient_4 = models.CharField(max_length=54, default='', blank=True)
    ingredient_5 = models.CharField(max_length=54, default='', blank=True)
    ingredient_6 = models.CharField(max_length=54, default='', blank=True)
    ingredient_7 = models.CharField(max_length=54, default='', blank=True)
    ingredient_8 = models.CharField(max_length=54, default='', blank=True)
    ingredient_9 = models.CharField(max_length=54, default='', blank=True)
    ingredient_10 = models.CharField(max_length=54, default='', blank=True)
    

    def __str__(self):
        return self.name 
        

