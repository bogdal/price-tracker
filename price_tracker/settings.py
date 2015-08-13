import os

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

MONGO_URI = os.environ.get('MONGO_URI')

HTTP_PROXY = os.environ.get('HTTP_PROXY')

SPIDER_URLS_FILE = os.environ.get(
    'SPIDER_URLS_FILE', os.path.join(PROJECT_ROOT, 'spider_urls.txt'))

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36',
    'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) '
        'like Gecko']

DOWNLOAD_DELAY = 2

ITEM_PIPELINES = {
    'price_tracker.crawler.pipelines.MongodbPipeline': 100}

DOWNLOADER_MIDDLEWARES = {
     'price_tracker.crawler.middlewares.RandomUserAgentMiddleware': 400,
     'price_tracker.crawler.middlewares.ProxyMiddleware': 410,
     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None}
