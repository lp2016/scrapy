# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

class TestSpider(scrapy.Spider):
    name = 'book2'
    start_urls = ['https://book.qidian.com/info/1010867586']

    def parse(self, response):
        item=TutorialItem()
        res=response.xpath('//div[@class="book-info "]/h1')
        item['name']= response.xpath('//div[@class="book-info "]/h1/em/text()').extract()[0]
        item['author']=res.xpath('//span/a[@class="writer"]/text()').extract()[0]
        item['bookType']=','.join(res.xpath('//p[@class="tag"]/a/text()').extract())
        item['wordCount']=res.xpath('//p/em/text()').extract()[0]
        item['description']=''.join(response.xpath('//div[@class="book-intro"]/p/text()').extract()).replace('\u3000','').strip()
        item['coverUrl']=response.xpath('//a[@id="bookImg"]/img/@src').extract()[0].strip()
        item['flag']=1

        yield  item
        yield scrapy.Request(url=self.start_urls[0]+'#Catalog',callback=self.getList)

    def getList(self, response):
        item=TutorialItem()
        res=response.xpath('//div[@class="volume"]')
        url_list = []
        if response.xpath('//div[@class="volume"][1]/h3/text()').extract()[1].strip() == '作品相关':
            for i in range(2,len(res)+1):
                url_list.extend(response.xpath('//div[@class="volume"][{}]//ul//li//a/@href'.format(i)).extract())
        else:
            for i in range(1,len(res)+1):
                url_list.extend(response.xpath('//div[@class="volume"][{}]//ul//li//a/@href'.format(i)).extract())
        chapterID = 1
        for url in url_list:
            item['chapterID']=chapterID
            yield scrapy.Request(url='https:'+url,callback=self.getContent,meta={'key':chapterID},errback=self.errback_httpbin)
            chapterID+=1

    def getContent(self,response):
        item=TutorialItem()
        item['chapterID']=response.meta['key']
        item['chapterName']=response.xpath('//div[@class="text-head"]/h3/text()').extract_first()
        item['chapterWordCount'] = response.xpath('//span[@class="j_chapterWordCut"]/text()').extract()[0]
        item['chapterUpdateTime'] = response.xpath('//span[@class="j_updateTime"]/text()').extract()[0]
        item['content'] = '\n'.join(response.xpath('//div[@class="read-content j_readContent"]/p/text()').extract())
        item['chapterUrl'] = response.url
        item['flag'] = 2
        yield item

    def errback_httpbin(self, failure):
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







