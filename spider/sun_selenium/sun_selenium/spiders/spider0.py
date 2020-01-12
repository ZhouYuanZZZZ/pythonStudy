# -*- coding: utf-8 -*-
import scrapy

from sun_selenium.items import SunSeleniumItem
from sun_selenium.logging_conf import logger


class Spider0Spider(scrapy.Spider):
    name = 'spider0'
    allowed_domains = ['d.wz.sun0769.com']

    def start_requests(self):
        for page in range(1, 482):
            url_prefix = 'http://d.wz.sun0769.com/index.php/department?departmentid=62&page='
            if page == 1:
                url = url_prefix
            else:
                url = url_prefix + str((page - 1) * 18)

            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        tr_list = response.xpath('//div[@class="newsHead clearfix"]/table[2]/tbody/tr')

        for tr in tr_list:
            no = tr.xpath('./td[1]/text()').extract_first()
            title = tr.xpath('./td[3]/a[1]/text()').extract_first()
            status = tr.xpath('./td[4]/span/text()').extract_first()

            item = SunSeleniumItem()
            item['no'] = no
            item['title'] = title
            item['status'] = status

            yield item
