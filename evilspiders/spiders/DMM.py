# -*- coding: utf-8 -*-
import scrapy
from evilspiders.items import DMMItem

class DmmSpider(scrapy.Spider):
    name = "DMM"
    allowed_domains = ["www.dmm.co.jp"]
    start_urls = (
        #'http://www.www.dmm.co.jp/',
        #'http://www.dmm.co.jp/mono/dvd/-/detail/=/cid=1star656/',
        #'/home/starling/1star658.html',
    )
    handle_httpstatus_list = [200,404]
    custom_settings = {
        'ITEM_PIPELINES': {
            'evilspiders.pipelines.MongoPipeline': 400,
    },
    #    'SPIDER_MIDDLEWARES': {
    #        'evilspiders.middlewares.DMM404SpiderMiddleware': 30,
    #}
    }

    def __init__(self, hinbans=None, hbfile=None):
        #self.handle_httpstatus_list.append(404)
        if hinbans:
            hbfile = None
            self.start_urls = ['http://www.dmm.co.jp/mono/dvd/-/detail/=/cid=%s/'%x for x in hinbans.split(',')]
        elif hbfile:
            hblist = [x.strip() for x in open(hbfile,'r').readlines()]
            self.start_urls = ['http://www.dmm.co.jp/mono/dvd/-/detail/=/cid=%s/'%x for x in hblist]
        else:
            self.start_urls = ['file:/home/starling/test.html']
        self.page404fpath = '/home/starling/DMM404list.txt'

    def parse(self, response):
        if response.status==404:
            with open(self.page404fpath,'a') as f:
                wronghinban = response.url.split('=')[-1].split('/')[0]
                f.write(wronghinban+'\n')
            return 

        item = DMMItem()
        item['title'] = response.xpath('//h1[@id="title"]/text()').extract()[0]
        item['page_url'] = response.url
        slist = response.xpath('//table[@class="mg-b20"]//tr/td[2]')
        item['date'] = slist[1].xpath('text()')[0].root
        item['runtime'] = slist[2].xpath('text()')[0].root
        #item['hinban'] = slist[9].xpath('text()')[0].root
        item['director'] = slist[4].xpath('node()/text()').extract()
        item['series'] = slist[5].xpath('a/text()') and slist[5].xpath('a/text()')[0].root or slist[5].xpath('text()')[0].root
        item['maker'] = slist[6].xpath('a/text()') and slist[6].xpath('a/text()')[0].root or slist[6].xpath('text()')[0].root
        item['label'] = slist[7].xpath('a/text()') and slist[7].xpath('a/text()')[0].root or slist[7].xpath('text()')[0].root
        item['actress'] = slist[3].xpath('span/node()/text()').extract()
        item['keyword'] = slist[8].xpath('a/text()').extract()
        item['image_url'] = response.xpath('//div[@id="sample-video"]//a[@name="package-image"]/@href')[0].extract()
        item['hinban'] = response.url.split('=')[-1].split('/')[0]
        yield item
