# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.utils.log import configure_logging


class A(scrapy.Spider):
    def __init__(self):
        print(self.name)
    def tt(self):
        print(self)
        configure_logging(install_root_handler=False)
        self.logger
        logging.basicConfig(
            filename='log.txt',
            format='%(levelname)s: %(message)s',
            level=logging.ERROR
        )
        self.logger.error('gfdgfdgdfg')
        self.logger.error('fffffffffff')


a=A()
a.tt()