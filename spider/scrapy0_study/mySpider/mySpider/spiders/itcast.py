# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        html = response.text
        html = BeautifulSoup(html)

        div_texts = html.select('div.tea_txt ul div.li_txt')

        for item in div_texts:

            h3 = item.select_one('h3').get_text().strip()
            h4 = item.select_one('h4').get_text().strip()
            p = item.select_one('p').get_text().strip()

            print(h3)
            print(h4)
            print(p)
            print('\n')

        print(len(div_texts))

    pass
