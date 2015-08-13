import random

from scrapy.utils.project import get_project_settings

settings = get_project_settings()


class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        request.headers.setdefault(
            'User-Agent', random.choice(settings.get('USER_AGENT_LIST')))


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = settings.get('HTTP_PROXY')
