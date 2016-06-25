# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KireinaItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    name = scrapy.Field()
    image_url = scrapy.Field()
    #pass

class DMMItem(scrapy.Item):
    hinban = scrapy.Field()
    title = scrapy.Field()
    actress = scrapy.Field()
    date = scrapy.Field()
    runtime = scrapy.Field()
    director = scrapy.Field()
    series = scrapy.Field()
    maker = scrapy.Field()
    label = scrapy.Field()
    keyword = scrapy.Field()
    image_url = scrapy.Field()
    page_url = scrapy.Field()
