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
        pass