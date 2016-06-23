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
    performer = scrapy.Field()
    date = scrapy.Field()
    series = scrapy.Field()
    maker = scrapy.Field()
    label = scrapy.Field()
    image_url = scrapy.Field()
