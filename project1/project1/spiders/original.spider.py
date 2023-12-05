import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["alibaba.com"]
    start_urls = ["https://alibaba.com"]

    def parse(self, response):
        pass
