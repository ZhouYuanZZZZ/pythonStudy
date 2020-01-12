import scrapy
from tecent_hr.logging_conf import logger
from bs4 import BeautifulSoup




class TecentHrSpider(scrapy.Spider):
    name = 'tecent_hr'
    allowed_domains = ['careers.tencent.com']
    start_urls = ['https://careers.tencent.com/search.html']

    def parse(self, response):
        logger.info('parse start')
        logger.info(response.text)
        items = response.xpath('/html/body/div/div[4]/div[3]/div[2]/div[2]/div/div[1]')
        logger.info(items)

        for item in items:
            logger.info("---------------------")
            title = item.xpath('./a/h4/text()').extract_first()
            logger.info(title)







