from Crawler import Crawler


class EbayCrawler(Crawler):

    def __init__(self):
        super(EbayCrawler,self).__init__()
        self.categories = {
            "Computer" : "https://www.ebay.in/sch/computer",
            "Cameras" : 
                  "https://ebay.in/sch/Cameras",  
            "Kitchen" : 
                  "https://www.ebay.in/sch/Kitchen",
            "Clothing" : "https://www.ebay.in/sch/clothing",
            "Footwear" : "https://www.ebay.in/sch/footwear",
            "Watches" : "https://www.ebay.in/sch/watches",
            "Mobile" : "https://www.ebay.in/sch/mobile",
            "Automobiles" : "https://www.ebay.in/sch/automobiles",
            "Toys" : "https://www.ebay.in/sch/toys",
            "Fashion Accessories" : "https://www.ebay.in/sch/accessories"
            }
  

    def get_product_links(self, url):
        print "Getting ebay links"
        new_url = url 
        product_links = []
        pgn=1
        while len(product_links) < 50:
            print pgn
            content = self.make_soup(new_url)
            for plinks in content.find_all('a',     
                    attrs = {'class' : 'vip'}):
                product_links.append(plinks.get('href'))
            pgn += 1
            new_url = url + '?&_pgn=' + str (pgn) 
        return product_links

    def get_product_details(self, urls, category):
        print "Getting details"
        details = []
        for url in urls:
            print "Getting url: ", url
            content = self.make_soup(url)
            try:
                price = content.find('span', attrs = {'id' : 'prcIsum'}).get('content')
            except:
                try:
                    content.find('span', attrs = {'id' : 'mm-saleDscPrc'}).text
                except:
                    price = None
            image = content.find('img', attrs = {'id' : 'icImg'}).get('src')
            name = content.find('meta', attrs = {'name' : 'description'}).get('content')
            details.append({'rating' : None, 'price' : price, 'image' : image,
                            'name' : name, 'category' : category, 'link' : url})
        return details

    def get_product_reviews(self, urls):
        reviews = []
        for url in urls:
            reviews.append({'link' : url, 'reviews' : []})

        return reviews
        