import os

SPIDER_URLS = [
    'http://www.ceneo.pl/Komputery;szukaj-wd+red+4tb',
    'http://www.ceneo.pl/;szukaj-thrustmaster',
]

CRAWLER = {
    'MONGO_URI': os.environ.get('MONGO_URI'),
    'DOWNLOAD_DELAY': 0.25,
    'ITEM_PIPELINES': {
        'price_tracker.crawler.pipelines.MongoPipeline': 100},
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
}
