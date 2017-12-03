import scrapy


class ProductsSpider(scrapy.Spider):
    name = "flipkart"

    def __init__(self, keyword=""):
        self.keyword = keyword

    def start_requests(self,keyword=''):
        url = "https://www.flipkart.com/search?q={}&otracker=start&as-show=on&as=off".format(self.keyword)
        print url, "###"
        return scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'flipkart_products.txt'
        with open(filename, 'wb') as f:
            f.write(response.xpath('//div/a/text()').extract())
        self.log('Saved file %s' % filename)
