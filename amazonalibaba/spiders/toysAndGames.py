# -*- coding: utf-8 -*-
import scrapy
from amazonalibaba.items import AmazonalibabaItem

class ToysandgamesSpider(scrapy.Spider):
    name = "toysAndGames"
    allowed_domains = ["amazon.com"]
    start_urls = [
        'https://www.amazon.com/Best-Sellers-Toys-Games/zgbs/toys-and-games/ref=zg_bs_toys-and-games_home_all?pf_rd_p=2140216822&pf_rd_s=center-1&pf_rd_t=2101&pf_rd_i=home&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=7BVWXC7HDN0EFA7DK0F6',
    ]

    def parse(self, response):
        for href in response.xpath('//*[@id="zg_centerListWrapper"]/div/div/div/a/@href'):
            url = href.extract().strip()
            yield scrapy.Request(url, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        #toysAndGames = tag
        tag = AmazonalibabaItem()
        for elem in response.xpath('//*[@id="productTitle"]/text()'):
            tag['title'] = elem.extract().strip()
        tag['price'] = response.xpath('//*[@id="priceblock_ourprice"]/text()').extract()
        tag['url'] = response.url
        yield tag
