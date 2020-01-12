# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import scrapy
from scrapy import signals
from sun_selenium.logging_conf import logger

from selenium import webdriver
from selenium.webdriver.common.by import By

# WebDriverWait 库，负责循环等待
from selenium.webdriver.support.ui import WebDriverWait

# expected_conditions 类，负责条件出发
from selenium.webdriver.support import expected_conditions as EC

from scrapy.http import HtmlResponse


class SeleniumMiddleware:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.set_page_load_timeout(5)
        self.wait = WebDriverWait(self.browser, 5)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):
        logger.info("chrome start")
        self.browser.get(request.url)

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="newsHead clearfix"]/table[2]/tbody/tr')))

        return HtmlResponse(url=request.url,
                            body=self.browser.page_source,
                            request=request,
                            encoding='utf-8',
                            status=200)

    @classmethod
    def from_crawler(cls, crawler):
        return cls()
