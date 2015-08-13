import os
os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'price_tracker.settings')

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from price_tracker.crawler.spiders import CeneoSpider


def run_crawler():
    process = CrawlerProcess(get_project_settings())
    process.crawl(CeneoSpider)
    process.start()
