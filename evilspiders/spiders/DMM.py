# -*- coding: utf-8 -*-
import scrapy
from evilspiders.items import DMMItem

class DmmSpider(scrapy.Spider):
    name = "DMM"
    allowed_domains = ["www.dmm.co.jp"]
    start_urls = (
        #'http://www.www.dmm.co.jp/',
        'http://www.dmm.co.jp/mono/dvd/-/detail/=/cid=1star656/',
    )

    def parse(self, response):
        item = DMMItem()
        item['title'] = response.xpath('//h1[@id="title"]/text()').extract()[0]
        slist = response.xpath('//table[@class="mg-b20"]//td[@width="100%"]')
        item['date'] = slist[1].xpath('text()')[0].root
        item['hinban'] = slist[9].xpath('text()')[0].root
        item['director'] = slist[4].xpath('a/text()')[0].root
        item['series'] = slist[5].xpath('a/text()')[0].root
        item['maker'] = slist[6].xpath('a/text()')[0].root
        item['label'] = slist[7].xpath('a/text()')[0].root
        item['actress'] = slist.xpath('span/a/text()').extract()
        item['image_url'] = response.xpath('//div[@id="sample-video"]//a[@name="package-image"]/@href')[0].extract()
        yield item
