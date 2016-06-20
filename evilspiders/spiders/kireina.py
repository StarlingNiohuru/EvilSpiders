# -*- coding: utf-8 -*-
import scrapy
from evilspiders.items import KireinaItem

class KireinaSpider(scrapy.Spider):
    name = "kireina"
    allowed_domains = ["http://kireina-megami.blog.jp",
                       #"http://blog.livedoor.jp",
    ]
    start_urls = (
        'http://kireina-megami.blog.jp/archives/52219528.html',
    )

    def parse(self, response):
        title = response.xpath('//h1[@class="article-title"]//a/text()').extract()[0]
        page_tag = '-'+title.split('-')[1]+'-'
        

        for sel in response.xpath('//div[@class="article-body"]/div[@align="center"]/a'):
            item = KireinaItem()
            item['title'] = title
            item['name'] = sel.xpath('@title').extract()[0]
            item['image_url'] = sel.xpath('@href').extract()[0]
            yield item

        next_node=response.xpath('//div[@class="article-body-inner"]/b[text()="%s"]/following-sibling::a[1]'%page_tag)
        if next_node:
            next_url = next_node[0].xpath('@href').extract()[0]

        yield scrapy.Request(next_url,callback=self.parse,dont_filter=True)
