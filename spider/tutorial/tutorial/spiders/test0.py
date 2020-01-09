# -*- coding: utf-8 -*-
import scrapy
from lxml import etree


class Test0Spider(scrapy.Spider):
    name = 'test0'
    allowed_domains = ['www.cma.gov.cn']
    start_urls = ['http://www.cma.gov.cn/2011xwzx/2011xqxxw/']

    def parse(self, response):
        html = etree.HTML(response.text)

        print('\n'*10)
        li_list = html.xpath('//*[@id="contains"]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li')
        print('----------------------li_list------------------------')
        print(type(li_list))
        print(len(li_list))

        for item in li_list:
           name = item.xpath('./a/text()')[0]
           date = item.xpath('./span/text()')[0]

           name = name.encode('utf-8')
           date = date.encode('utf-8')

           name = str(name,'utf-8')
           date = str(date, 'utf-8')

           print(name +' '+date)

        return []
