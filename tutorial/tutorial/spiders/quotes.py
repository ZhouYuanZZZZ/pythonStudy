import scrapy
from bs4 import BeautifulSoup
from tutorial.tutorial.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        html = BeautifulSoup(response.body, "lxml")
        quotes =  html.select('.quote')

        for quote in quotes:

            item = QuoteItem()
            item['text'] = quote.select_one('span.text')
            item['author'] = quote.select_one('.author')
            item['tags'] = quote.select_one('.tags .keywords')
            print(item)
            yield item

        next = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)
