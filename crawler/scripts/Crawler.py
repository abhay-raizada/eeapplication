import requests
from bs4 import BeautifulSoup


class Crawler(object):

    def __init__(self):
        pass

    def open_by_category(self, category):
        url = self.categories[category]
        print "Getting products"
        product_links = self.get_product_links(url)
        print "Getting reviews"
        reviews = self.get_product_reviews(product_links)
        print "Getting product details"
        details = self.get_product_details(product_links, category)

        return {'details' : details, 'reviews' : reviews}

    @staticmethod
    def make_soup(url):
        response = requests.get(
            url,
            headers={'User-agent': 'eecrawler'})

        html = response.content
        return BeautifulSoup(html, "html.parser")

    def get_product_links(self, url):
        pass

    def get_product_reviews(self, urls):
        pass

    def get_product_details(self, url):
        pass
    