# -*- coding: utf-8 -*-

# Define here the models for your scraped item loaders
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/loaders.html#input-and-output-processors

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


class ScrapingTestingLoader(ItemLoader):
    default_input_processor = MapCompose(unicode.strip)
    default_output_processor = TakeFirst()
