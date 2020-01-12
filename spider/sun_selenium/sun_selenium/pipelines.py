# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sun_selenium.logging_conf import logger
class SunSeleniumPipeline(object):
    def process_item(self, item, spider):
        logger.info(item)

        return item
