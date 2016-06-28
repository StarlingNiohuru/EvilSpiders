# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib2
import os
import pymongo
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings

class ImagePipeline(object):

    def __init__(self):
        self.path = '/home/starling/kireina/'
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        actress = item['title'].split('-')[0]
        fname = self.path+actress+'/'+item['title']+'/'+item['name']+'.jpg'
        fpath1 = self.path+actress+'/'
        fpath2 = fpath1+item['title']+'/'
        if not os.path.exists(fpath1):
            os.mkdir(fpath1)
        if not os.path.exists(fpath2):
            os.mkdir(fpath2)

        with open(fname,'wb') as fw:
            res = urllib2.urlopen(item['image_url'])
            fw.write(res.read())
            fw.close()
        return item

class MongoPipeline(object):

    def __init__(self):
        cr = CrawlerRunner(get_project_settings())
        client = pymongo.MongoClient(cr.settings['MONGODB_HOST'], cr.settings['MONGODB_PORT'])
        db = client[cr.settings['MONGODB_DATABASE']]
        self.collection = db[cr.settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
	self.collection.insert_one(dict(item))
	log.msg("Item wrote to MongoDB database {}, collection {}, at host {}, port {}".format(
	    cr.settings['MONGODB_DATABASE'],
	    cr.settings['MONGODB_COLLECTION'],
	    cr.settings['MONGODB_HOST'],
	    cr.settings['MONGODB_PORT']))
	return item
