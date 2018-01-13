# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['https://read.qidian.com/chapter/UHfWGYSG8AaoUTngny7bXQ2/zlLPtEoMyKJp4rPq4Fd4KQ2']

    def parse(self, response):
        print("here")


