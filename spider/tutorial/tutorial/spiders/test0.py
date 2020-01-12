# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from tutorial.logging_conf import logger
from tutorial.items import TutorialItem


class Test0Spider(scrapy.Spider):
    name = 'test0'
    allowed_domains = ['www.cma.gov.cn']
    start_urls = ['http://www.cma.gov.cn/2011xwzx/2011xqxxw/']

    def parse(self, response):
        li_list = response.xpath('//*[@id="contains"]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li')

        logger.info('li size:{}'.format(len(li_list)))

        for item in li_list:
            name = item.xpath('./a/text()').extract_first()
            date = item.xpath('./span/text()').extract_first()

            logger.info('{}-{}'.format(name,date))


        return []
