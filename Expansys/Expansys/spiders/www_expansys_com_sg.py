import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from ..items import ExpansysItem

class WwwExpansysComSg(CrawlSpider):
    name = 'www_expansys_com_sg_crawler'
    allowed_domains = ['expansys.com.sg']
    start_urls = ['http://www.expansys.com.sg/']
    rules =(Rule(
      LinkExtractor(
        allow = (
          r'.+/\S+-\d+/', 
        ),
        deny = (
          r'.+/?filter',
        )
      ),
      callback = 'parse_categories',
      follow = True),
      )
      
    def parse_categories(self,response):
        #l = ItemLoader(item=ExpansysItem(), response=response)
        _title = response.xpath('//div[@id="product"]//h1[@itemprop="name"]/text()').extract()
        _url = response.url
        _price = response.xpath('//p[@id ="price"]//span/text()').extract()
        _price = _price + response.xpath('//p[@id ="price"]//span/sup/text()').extract()
        _model = response.xpath('//ul[@class ="product-sku"]/li[4]/span/text()').extract()
        _sku = response.xpath('//ul[@class ="product-sku"]/li[1]/span/text()').extract()
        _mpn = response.xpath('//ul[@class ="product-sku"]/li[3]/span/text()').extract()
        #_upc =
        _ean = response.xpath('//ul[@class ="product-sku"]/li[2]/span/text()').extract()
        _currency = response.xpath('//p[@id ="price"]/meta/@content').extract()
        #_crawl_time =
        #_image_urls = 
        #_categories =
        _instock = response.xpath('//li[@id ="stock"]/text()').extract()
        if _title:
            print '----------------------------------------------------'
            print _title
            print _url
            print _price
            print _currency
            print _instock
            print _sku
        #l.add_xpath('_name', '//div[@id="product"]//h1[@itemprop="name"]/text()')
        #l.add_xpath('price', '//p[@id="price"]')
        #l.add_css('stock', 'p#stock]')
        #l.add_value('last_updated', 'today') # you can also use literal values
        #return l.load_item()