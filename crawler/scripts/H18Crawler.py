from Crawler import Crawler


class H18Crawler(Crawler):

    def __init__(self):
        super(H18Crawler,self).__init__()
        self.categories = {
            "Computer" : "http://www.homeshop18.com/computer/computers-tablets/categoryid:3254/search:computer/r",
            "Cameras" : 
                "http://www.homeshop18.com/camera/categoryid:3159/search:camera",  
            "Kitchen" : 
                  "http://www.homeshop18.com/kitchen/categoryid:3503/search:kitchen",
            "Clothing" : "http://www.homeshop18.com/clothing/categoryid:3396/search:clothing/",
            "Footwear" : "http://www.homeshop18.com/footwear/categoryid:15051/search:footwear/",
            "Watches" : "http://www.homeshop18.com/watches/categoryid:15197/search:watches",
            "Mobile" : "http://www.homeshop18.com/mobile/categoryid:3024/search:mobile/sort:Customer+Ratings/",
            "Automobiles" : "http://www.homeshop18.com/automobiles/categoryid:17143/search:automobiles/",
            "Toys" : "http://www.homeshop18.com/toys/categoryid:3335/search:toys/",
            "Fashion Accessories" : 
                "http://www.homeshop18.com/accessories/categoryid:15095/search:accessories/"
            }


    def get_product_links(self, url):
        print "Getting H18 links"
        product_links = []
        new_url = url
        page = 24
        while len(product_links) < 50:
            print page, len(product_links)
            content = self.make_soup(new_url)
            for plinks in content.find_all('a', 
                    attrs = {'class' : 'productTitle'}):
                print("http://www.homeshop18.com" + plinks.get('href'))
                product_links.append("http://www.homeshop18.com" + plinks.get('href'))
            print "End Page"
            new_url = url + '/start:' + str(page)
            page += 24

        return product_links

    def get_product_details(self, urls, category):
        details = []
        for url in urls:
            print "Getting url: ", url
            content = self.make_soup(url)
            try:
                rating = content.find('div', attrs = {'id' : "avgProductRatingPDPDiv"})
                rating = rating.text
            except:
                rating = None
            try:
                price = content.find('span', attrs= {'id' : 'hs18Price'}).text
            except:
                price = None
            image = content.find('img', attrs = {'id' : 'pbilimage1tag'}).get('src')
            name = content.find('title').text
            details.append({'rating' : rating, 'price' : price, 'image' : image,
                            'name' : name, 'category' : category, 'link' : url})

        return details

    def get_product_reviews(self, urls):
        reviews_list = []
        print "Starting reviews"
        for url in urls:
            print "For URL ", url
            content = self.make_soup(url)
            try:
                review_url = content.find('div', attrs = {'id' : 'productReviewCountPDPDiv'})
                review_url = "http://www.homeshop18.com" + review_url.find('a').get('href')
            except:
                reviews_list.append({'link' : url, 'reviews' : []})
                continue
            reviews_page = self.make_soup(review_url)
            reviews = reviews_page.find('ul', attrs = {'id' : 'reviews'})
            recommend = reviews.find('div', attrs = {'class' : 'percentage'})
            recommend = recommend.find('strong').text
            stars = reviews.find('div', attrs = {'class' : 'star_fix'})
            number_of_reviews = stars.text
            print number_of_reviews
            rating = None
            for star in stars.find_all('span'):
                if star.get('class'):
                    rating = star.get('class')[0]

            dictr= {'link' : url, 'reviews' : [recommend, 
                        number_of_reviews, rating]}
            print dictr
            reviews_list.append(dictr)

        return reviews_list