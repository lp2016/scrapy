# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

class OnlytestSpider(scrapy.Spider):
    name = 'onlytest'

    def start_requests(self):
        url = 'http://quotes.toscrape.com/page/1/'


        yield scrapy.Request(url=url, callback=self.parse,errback=self.errback_httpbin)

    def parse(self, response):

        self.logger.info('Saved file ')
    def errback_httpbin(self, failure):
        # log all failures

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)







