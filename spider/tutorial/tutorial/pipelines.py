# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from tutorial.logging_conf import logger


class TutorialPipeline0(object):
    def process_item(self, item, spider):

        logger.info('{}-{}'.format(item['name'], item['date']))

        return item
