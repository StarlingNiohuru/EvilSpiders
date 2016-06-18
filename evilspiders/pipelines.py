# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib2
import os

class ImagePipeline(object):

    def __init__(self):
        self.path = '/home/starling/testpath/'
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        fname = self.path+item['name']+'.jpg'
        with open(fname,'wb') as fw:
            res = urllib2.urlopen(item['image_url'])
            fw.write(res.read())
            fw.close()
        return item
