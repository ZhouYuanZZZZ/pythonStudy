import scrapy
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class TecentHrSpider(scrapy.Spider):
    name = 'tecent_hr'
    allowed_domains = ['careers.tencent.com']
    start_urls = ['http://careers.tencent.com/search.html?query=co_1&sc=1']

    def parse(self, response):
        logger.info('parse start')

        html = response.text
        html = BeautifulSoup(html)

        positions = html.select('div.recruit-list a h4')

        for item in positions:
            position_text = item.get_text().strip()

            item_object = {'position_text', position_text}

            yield item_object

        # 找到下一页的url地址
        page_index = html.select('ul.page-list li.active span').item.get_text().strip()
        page_index = int(page_index)
        next_url = 'http://careers.tencent.com/search.html?query=co_1&sc=1&index=' + page_index + 1;

        if page_index != 407:
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                # meta = {"item":item}
            )
