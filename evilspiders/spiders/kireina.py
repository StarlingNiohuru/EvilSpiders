# -*- coding: utf-8 -*-
import scrapy
from evilspiders.items import KireinaItem

class KireinaSpider(scrapy.Spider):
    name = "kireina"
    allowed_domains = ["http://kireina-megami.blog.jp",
                       #"http://blog.livedoor.jp",
    ]
    start_urls = (
        'http://kireina-megami.blog.jp/archives/54386797.html',
    )

    def parse(self, response):
        title = response.xpath('//h1[@class="article-title"]//a/text()').extract()[0]
        page_num = title.split('-')[1]

        for sel in response.xpath('//div[@align="center"]/a'):
            item = KireinaItem()
            item['title'] = title
            item['name'] = sel.xpath('@title').extract()[0]
            item['image_url'] = sel.xpath('@href').extract()[0]
            yield item

        for sel in response.xpath('//div[@class="article-body-inner"]/a'):
            url=sel.xpath('@href').extract()[0]
            if 'cat' in url:
                continue 
            num=sel.xpath('b/text()').extract()[0][1:-1]
            if int(page_num)+1==int(num):
                next_url = 'http://kireina-megami.blog.jp/archives/'+url.split('/')[-1]
                break
        yield scrapy.Request(next_url,callback=self.parse,dont_filter=True)
