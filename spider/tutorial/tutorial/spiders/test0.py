# -*- coding: utf-8 -*-
import scrapy


class Test0Spider(scrapy.Spider):
    name = 'test0'
    allowed_domains = ['www.cma.gov.cn']
    start_urls = ['http://www.cma.gov.cn/2011xwzx/2011xqxxw/']

    def parse(self, response):
        print(response.text)
