import sys
import tarfile
from scrapy.crawler import CrawlerProcess
from evilspiders.spiders.kireina import KireinaSpider
from scrapy.utils.project import get_project_settings

def run(url):
    process = CrawlerProcess(get_project_settings())
    process.crawl(KireinaSpider, start_urls=[url])
    process.start()

def tarpath(rpath='/home/starling/'):
    tf=tarfile.open('%skireina.tar'%rpath,'w')
    tf.add('%skireina/'rpath)
    tf.close()

if __name__=='__main__':
    url = sys.argv[1]
    run(url)
    tarpath()
