# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Reviews(models.Model):
    link = models.CharField(max_length=200, primary_key = True)
    rating = models.CharField(max_length=200, null = True)
    recommend = models.CharField(max_length=200, null = True)
    number_of_reviews = models.CharField(max_length = 200, null = True)
    
class Products(models.Model):
    name = models.CharField(max_length=200)
    rating = models.CharField(max_length=200, null = True)
    link = models.CharField(max_length=200, primary_key = True)
    image = models.CharField(max_length=200, null = True)
    price = models.CharField(max_length=200, null = True)
    category = models.CharField(max_length=200)
    reviews = models.ForeignKey(Reviews, on_delete=models.CASCADE, null = True)




# Create your models here.
