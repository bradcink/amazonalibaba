# -*- coding: utf-8 -*-
import scrapy
from amazonalibaba.items import AmazonalibabaItem


class BestsellersSpider(scrapy.Spider):
    name = "bestSellers"
    allowed_domains = ["amazon.com"]
    start_urls = [
        'https://www.amazon.com/Best-Sellers/zgbs',
    ]

    def parse(self, response):
        for href in response.xpath('//*[@id="zg_left_col1"]/div/div/a/@href'):
            url = href.extract().strip()
            yield scrapy.Request(url, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        #toysAndGames = tag
        tag = AmazonalibabaItem()

        for price in response.xpath('//*[@id="zg_centerListWrapper"]/div/div/div/div/strong'):
            tag['price'] = price.xpath('text()').extract().strip()
        for link in response.xpath('//*[@id="zg_centerListWrapper"]/div/div/div/a'):
            tag['title'] = link.xpath('text()').extract().strip()
            tag['url'] = link.xpath('@href').extract().strip()
        yield tag
