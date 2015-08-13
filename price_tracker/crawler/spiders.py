from datetime import datetime
import os

from scrapy import Request, Spider


class CeneoSpider(Spider):

    name = 'ceneo'

    def start_requests(self):
        file_name = self.settings.get('SPIDER_URLS_FILE')
        if os.path.exists(file_name):
            handler = open(file_name)
            self.start_urls = handler.read().splitlines()
        return super(CeneoSpider, self).start_requests()

    def parse(self, response):
        for url in response.css('div.cat-prod-row-desc a.js_conv::attr("href")'):
            yield Request(response.urljoin(url.extract()), self.parse_product)
        next_page_url = response.css('.pagination .arrow-next a::attr("href")')
        if next_page_url:
            url = response.urljoin(next_page_url.extract()[0])
            yield Request(url, self.parse)

    def parse_product(self, response):
        item = {
            'url': response.url,
            'name': response.css('h1.product-name::text').extract()[0],
            'price': response.css('div.aggregate-offer .price::text').extract()[0],
            'date': datetime.now(),
            'offers': []}
        for product in response.css('table tr.product-offer'):
            shop = product.css('td.cell-store-logo img::attr("alt")')
            if not shop:
                shop = product.css('td.cell-store-logo .displayed-shop-name::text')
            item['offers'].append({
                'offer_id': product.css('::attr("data-offer")').extract()[0],
                'shop_id': product.css('::attr("data-shop")').extract()[0],
                'shop': shop.extract()[0],
                'name': product.css('td.cell-product span::text').extract()[0],
                'price': product.css('td.cell-price strong::text').extract()[0]})
        yield item
