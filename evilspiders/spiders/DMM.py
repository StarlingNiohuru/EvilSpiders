# -*- coding: utf-8 -*-
import scrapy


class DmmSpider(scrapy.Spider):
    name = "DMM"
    allowed_domains = ["www.dmm.co.jp"]
    start_urls = (
        'http://www.www.dmm.co.jp/',
    )

    def parse(self, response):
        pass
