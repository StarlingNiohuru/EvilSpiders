# -*- coding: utf-8 -*-

class DMM404SpiderMiddleware(object):

    def __init__(self):
        self.opath = '/home/starling/DMM404list.txt'

    #def process_exception(self, exception, spider):
    #    pass

    def process_response(self, response, spider=None):
        if response.status==404:
            with open(self.opath,'a') as f:
                hinban = response.url.split('=')[-1].split('/')[0]
                f.write(hinban+'\n')
        return 
