import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class WwwExpansysComSg(CrawlSpider):
  name = 'www_expansys_com_sg_crawler'
  allowed_domains = ['expansys.com.sg']
  start_urls = ['http://www.expansys.com.sg/']