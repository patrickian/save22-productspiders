import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from ..items import ExpansysItem

class WwwExpansysComSg(CrawlSpider):
    name = 'www_expansys_com_sg_crawler'
    allowed_domains = ['expansys.com.sg']
    start_urls = ['http://www.expansys.com.sg/']
    rules =(Rule(LinkExtractor(allow = (r'/\S+-\d+/', 
        )) , #restrict_xpaths=('//div[@id = "nav"]/ul/li')),
        callback = 'parse_categories', follow = True),
      )
    #, deny =(''))
    def parse_categories(self,response):
        l = ItemLoader(item=ExpansysItem(), response=response)
        print '----------------------------------------------------'
        print response
        l.add_xpath('_name', '//div[@id="product"]//h1[@itemprop="name"]/text()')
        #l.add_xpath('price', '//p[@id="price"]')
        #l.add_css('stock', 'p#stock]')
        #l.add_value('last_updated', 'today') # you can also use literal values
        return l.load_item()