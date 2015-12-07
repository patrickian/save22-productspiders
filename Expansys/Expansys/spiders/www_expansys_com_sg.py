import scrapy
from datetime import datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from ..items import ExpansysItem

class WwwExpansysComSg(CrawlSpider):
    name = 'www_expansys_com_sg_crawler'
    allowed_domains = ['expansys.com.sg']
    start_urls = ['http://www.expansys.com.sg/']
    rules =(
      Rule(LinkExtractor(allow = (r'.+', ),deny = ( r'.+/?filter\S+',r'.+aspx.\S+',r'.+/forum.\S+',r'.+/blog\S+',r'.+/?c=\S+',r'.+/more/\S+')),callback = 'parse_products',follow = True),
      #Rule(LinkExtractor( allow = (r'.+/?page=[1-9]+#\w+',),deny = (r'.+/?filter',)),follow = True),
      #Rule(LinkExtractor( allow = (r'.+/\S+-\d+.',), deny = ( r'.+/?filter\S+',)),callback = 'parse_products', follow = False),
      )
    
    def parse_categories(self,response):
        pass
    
    def parse_products(self,response):
        print 'PUMASOK ------------------------------------------------------------'
        _upc = []
        _sku = []
        _ean = []
        _mpn = []
        _title = response.xpath('//div[@id="product"]/div/h1[@itemprop="name"]/text()').extract()
         
        print _title
        print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!asdasdasd' 
        #_prod = response.xpath('//ul[@class ="product-sku"]/li/span/@content').extract() 
        #for x in _prod: 
        #  if x[0:3] == 'sku': _sku.append(x[4:])
        #  elif x[0:3] == 'ean': _ean.append(x[4:])
        #  elif x[0:3] == 'upc': _upc.append(x[4:])
        #  elif x[0:3] == 'mpn': _mpn.append(x[4:]) 
          
        if _title:
          item = ExpansysItem()
          _price = response.xpath('//p[@id ="price"]/strong/span/text()').extract()[0]
          item['_title'] = response.xpath('//div[@id="product"]//h1[@itemprop="name"]/text()').extract()
          item['_url'] = response.url 
          item['_price'] = _price + response.xpath('//p[@id ="price"]/strong/span/sup/text()').extract()[0]
          item['_model'] = response.xpath('//ul[@class ="product-sku"]//a[@itemprop ="brand"]/text()').extract()          
          item['_currency'] = response.xpath('//p[@id ="price"]/meta/@content').extract()
          item['_crawl_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          item['_image_urls'] = response.xpath('//div[@id ="image"]//img/@src').extract()
          _cat = response.xpath('//ul[@id ="breadcrumbs"]/li[@class ="level_0"]//span/text()').extract()
          _cat.extend(response.xpath('//ul[@id ="breadcrumbs"]/li[@class ="level_1"]//span/text()').extract())
          item['_categories'] = '\\'.join(_cat)
          item['_instock'] = response.xpath('//li[@id ="stock"]/text()').extract()
          yield item
        