# -*- coding: utf-8 -*-

class DMM404DownloaderMiddleware(object):

    def __init__(self, crawler):

    def process_exception(self, request, exception, spider):
        return_request = change_proxy(request)
        if return_request: 
            return return_request

    def process_response(self, request, response, spider):
        if response.status==404:
            return_request = change_proxy(request)
            if return_request: 
                return return_request
        return response
