# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['https://read.qidian.com/chapter/UHfWGYSG8AaoUTngny7bXQ2/zlLPtEoMyKJp4rPq4Fd4KQ2']

    def parse(self, response):
        yield scrapy.Request(url='https://read.qidian.com/chapter/',callback=self.parse_test,errback=self.error_back)
        yield scrapy.Request(url='https://read.qidian.com/chapte2dr/',callback=self.parse_test,errback=self.error_back)


    def parse_test(self,response):
        print("+"*30)
        pass


    def error_back(self,response):
        with open('error2.txt','a') as f:
            f.write(response.value.response.url)
            f.write('\n')



