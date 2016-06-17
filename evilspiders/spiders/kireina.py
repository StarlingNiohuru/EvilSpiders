# -*- coding: utf-8 -*-
import scrapy
from evilspiders.items import KireinaItem

class KireinaSpider(scrapy.Spider):
    name = "kireina"
    allowed_domains = ["http://kireina-megami.blog.jp"]
    start_urls = (
        'http://kireina-megami.blog.jp/archives/54453388.html',
    )

    def parse(self, response):
        for sel in response.xpath('//div[@align="center"]/a'):
            item = KireinaItem()
            item['name'] = sel.xpath('@title').extract()[0]
            item['image_url'] = sel.xpath('@href').extract()[0]
            yield item
        #fpath = 'midori_satsuki'
        #with open(fpath, 'wb') as f:
        #    res=urllib2.urlopen(item['image_url')
        #    f.write(res.read())
        #    f.close()
