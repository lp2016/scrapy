# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    #书名
    name=scrapy.Field()
    #简介
    description = scrapy.Field()
    #作者名
    author=scrapy.Field()
    #类型
    bookType=scrapy.Field()
    #上架时间
    startTime=scrapy.Field()
    #书的总字数
    wordCount=scrapy.Field()
    #封面
    coverUrl=scrapy.Field()
    #章节名称
    chapterName=scrapy.Field()
    #章节ID
    chapterID=scrapy.Field()
    #章节字数
    chapterWordCount=scrapy.Field()
    #内容
    content=scrapy.Field()
    #章节更新时间
    chapterUpdateTime=scrapy.Field()
    #章节来源
    chapterUrl=scrapy.Field()
    #爬取时间
    time=scrapy.Field()
    #item标志
    flag=scrapy.Field()




