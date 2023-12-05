import scrapy


class SpiderAlibaba1Spider(scrapy.Spider):
    name = "spider_alibaba1"
    allowed_domains = ["alibaba.com"]
    start_urls = ["https://alibaba.com"]

    def parse(self, response):
        pass
