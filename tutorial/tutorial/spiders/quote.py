# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quote'
    start_urls = ['https://book.qidian.com/info/1010736700']

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
        url="https:"+response.xpath('//div[@class="book-info "]/p/a[@class="red-btn J-getJumpUrl "]/@data-firstchapterjumpurl').extract()[0]


        yield item
        yield scrapy.Request(url=url,callback=self.parse_getChapterContent)



    def parse_GetChapterUrl(self,response):
        url='https://'+response.xpath('//div[@class="volume-wrap"]/div[@class="volume"][2]/ul/li[1]/a/@href').extract()[0]

        yield scrapy.Request(url=url,callback=self.parse_getChapterContent)

    def parse_getChapterContent(self,response):
        item=TutorialItem()
        nextChapterUrl =response.xpath('//div[@class="chapter-control dib-wrap"]/a[@id="j_chapterNext"]/@href').extract()
        if nextChapterUrl:
            res = response.xpath('//div[@class="text-head"]')
            item['chapterName'] = res.xpath('.//h3/text()').extract()[0]
            item['chapterWordCount']=response.xpath('//span[@class="j_chapterWordCut"]/text()').extract()[0]
            item['chapterUpdateTime']=response.xpath('//span[@class="j_updateTime"]/text()').extract()[0]
            item['content']='\n'.join(response.xpath('//div[@class="read-content j_readContent"]/p/text()').extract())
            item['chapterUrl']=response.url
            item['flag']=2

            yield item
            #yield scrapy.Request(url='https://'+nextChapterUrl[0],callback=self.parse_getChapterContent,errback=self.err_back)

    def err_back(self,response):
        with open('error.txt','a') as f:
            f.write(response.value.response.url)
            f.write('\n')






        #yield item
