# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.shortcuts import render
from crawler.scripts.H18Crawler import H18Crawler
from crawler.scripts.EbayCrawler import EbayCrawler
from crawler.models import Products,Reviews
from django.template import Context

def add_to_db(details):
    print(len(details))
    #print "adding", detail, reviews, "to db"
    for detail, review in zip(details['details'], details['reviews']):
        if review['reviews'] != []:
            r = Reviews(link = review['link'], rating = review['reviews'][2], 
                    recommend = review['reviews'][0], 
                    number_of_reviews = review['reviews'][1])
            p = Products(name = detail['name'] ,rating = detail['rating'] ,
                image = detail['image'] ,link = detail['link'], 
                price = detail['price'], category = detail['category'],
                reviews = r)
            r.save()
            p.save()
        else: 
            p = Products(name = detail['name'] ,rating = detail['rating'] ,
             image = detail['image'] ,link = detail['link'], 
             price =detail['price'], category = detail['category'],
             reviews = None)
            p.save()
    details = []

def save():
    categories = ["Computer", "Cameras", "Kitchen", "Clothing", "Footwear", 
                  "Watches"]
    ebay_crawler = EbayCrawler()
    h18_crawler = H18Crawler()
    for category in categories:
        print "Getting category: ", category
        add_to_db(h18_crawler.open_by_category(category))
        add_to_db(ebay_crawler.open_by_category(category))

def index(request):
    save()
    return HttpResponse("Added to db succesfully")

def website(request):
    print(request.method)
    categories = ["Computer", "Cameras", "Kitchen", "Clothing", "Footwear"]

    #context = {'computers'  : computers
    category = None
    start_page = 0
    if request.GET.get('category'):
        category = request.GET.get('category')
        try:
            start_page = int(request.GET.get('start_page')) -1
        except:
            start_page = 0
        products = Products.objects.filter(category=category)[start_page:start_page + 24]
        context = {'products'  : products, "category" : category, "categories" : categories}
        return render_to_response("crawler/website.html", context)
    if request.GET.get('start_page'):
        start_page = int(request.GET.get('start_page')) -1
        print "Catergory is ", category
        products = Products.objects.filter(category=category)[start_page:start_page + 24]
        context = {"products" : products, "category" : category, "categories" : categories}
        return render_to_response("crawler/website.html", context)

    print start_page
    products = Products.objects.filter(category=category if category else "Computer")[start_page*24: start_page + 24]
    return render_to_response("crawler/website.html", {"products" : products, 
                                                       "category" : category,
                                                       "categories" : categories})

