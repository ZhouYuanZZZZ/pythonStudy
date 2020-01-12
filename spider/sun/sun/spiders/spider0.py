# -*- coding: utf-8 -*-
import scrapy

from sun.items import SunItem
from sun.logging_conf import logger
from sun.pipelines import SunPipeline


class Spider0Spider(scrapy.Spider):
    name = 'spider0'
    allowed_domains = ['d.wz.sun0769.com']
    start_urls = ['http://d.wz.sun0769.com/index.php/department?departmentid=62']

    next_page_count = 18

    def parse(self, response):
        tr_list = response.xpath('//div[@class="newsHead clearfix"]/table[2]/tr')

        for tr in tr_list:
            no = tr.xpath('./td[1]/text()').extract_first()
            title = tr.xpath('./td[3]/a[1]/text()').extract_first()
            status = tr.xpath('./td[4]/span/text()').extract_first()

            item = SunItem()
            item['no'] = no
            item['title'] = title
            item['status'] = status

            yield item

        next_page_prefix = 'http://d.wz.sun0769.com/index.php/department?departmentid=62&page='
        next_page = next_page_prefix + str(Spider0Spider.next_page_count)
        Spider0Spider.next_page_count = Spider0Spider.next_page_count + 18

        logger.info(Spider0Spider.next_page_count)
        logger.info(next_page)


        if (next_page != 'http://d.wz.sun0769.com/index.php/department?departmentid=62&page=8640'):
            logger.info('next page')
            yield scrapy.Request(next_page, callback=self.parse)
