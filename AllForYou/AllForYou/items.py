# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AllforyouItem(scrapy.Item):
    # define the fields for your item here like:
    _title = scrapy.Field()
    _price = scrapy.Field()
    _out_of_stock = scrapy.Field()
    _retailer_sku = scrapy.Field()
    _primary_img_url = scrapy.Field()
    _description = scrapy.Field()
    _url = scrapy.Field()
    _categories = scrapy.Field()
    _crawlTime = scrapy.Field()
    _offer = scrapy.Field()