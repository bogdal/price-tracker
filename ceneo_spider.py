from datetime import datetime

import scrapy


class CeneoSpider(scrapy.Spider):
    name = 'ceneo'
    start_urls = ['http://www.ceneo.pl/Komputery;szukaj-wd+red+4tb']

    def parse(self, response):
        for url in response.css('div.cat-prod-row-desc a.js_conv::attr("href")'):
            yield scrapy.Request(response.urljoin(url.extract()), self.parse_product)

    def parse_product(self, response):
        for product in response.css('table tr.product-offer'):
            yield {
                'url': response.url,
                'product_name': response.css('h1.product-name::text').extract()[0],
                'name': product.css('td.cell-product span::text').extract()[0],
                'shop_id': product.css('::attr("data-shop")').extract()[0],
                'shop': product.css('td.cell-store-logo img::attr("alt")').extract()[0],
                'price': product.css('td.cell-price strong::text').extract()[0],
                'date': datetime.now(),
                'offer_id': product.css('::attr("data-offer")').extract()[0]}

