from unittest.mock import call
import scrapy


class NewsSpider(scrapy.Spider):

    name = "news"

    def start_requests(self):
        urls = [
            'https://www.bbc.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]

        filename = f'news.html {page}'

        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
