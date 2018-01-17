# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import scrapy
import os
from tutorial.settings import IMAGES_STORE as images_store
from scrapy.pipelines.images import ImagesPipeline
book_path=r'C:\Users\LGH\Anaconda3\scrapy\tutorial\tutorial\book'
image_path=''
data = {
    "info": {},
    "chapter": []

}
class TutorialPipeline(object):


    def __init__(self):
        self.f=open("book.json","w")
    def process_item(self, item, spider):
        if item['flag'] == 1:
            data["info"]["name"]=item["name"]
            data["info"]["author"]=item["author"]
            data["info"]["bookType"]=item["bookType"]
            data["info"]["wordCount"]=item["wordCount"]
            data["info"]["description"]=item["description"]
            self.book_name=item['name']
        else:
            ch={}
            ch["chapterName"]=item["chapterName"]
            ch["chapterID"]=item["chapterID"]
            ch["chapterUpdateTime"]=item["chapterUpdateTime"]
            ch["chapterWordCount"]=item["chapterWordCount"]
            ch["chapterUrl"]=item["chapterUrl"]
            ch["content"]=item["content"]
            data["chapter"].append(ch)
        return item

    def close_spider(self,spider):
        content = json.dumps(data, ensure_ascii=False, indent=4)
        self.f.write(content.encode("utf-8").decode("utf-8") )
        self.f.close()
        os.renames('book.json', book_path + r'\book\\' + self.book_name + '.json')
        os.renames(images_store + image_path, book_path + r'\book\\' + self.book_name + ".jpg")
        os.renames(book_path+r"\book", book_path + r"\\"+ self.book_name )


class ImgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if item['flag'] ==1:
            yield scrapy.Request("https:" + item['coverUrl'])


    #当下载请求完成后执行该方法
    def item_completed(self, results, item, info):
        if results:
            global image_path
            image_path = results[0][1]["path"]
        return item

class TestPipeline(object):

    def __init__(self):
        print('fdfd')
    def process_item(self, item, spider):
        print(item['chapterName'])
        return item
