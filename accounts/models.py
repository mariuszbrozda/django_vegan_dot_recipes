# Create your models here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_description = models.TextField(max_length=400, default='')
    user_city =  models.CharField(max_length=40, default='')
    user_image = models.ImageField(upload_to='images')
    
    
    def __str__(self):
        return self.name 