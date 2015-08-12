from scrapy.crawler import CrawlerProcess

from price_tracker.crawler.spiders import CeneoSpider
from price_tracker.settings import CRAWLER as crawler_settings


def run_crawler():
    process = CrawlerProcess(crawler_settings)
    process.crawl(CeneoSpider)
    process.start()
