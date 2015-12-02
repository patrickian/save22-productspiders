import scrapy
from datetime import datetime
from ..items import AllforyouItem

class WwwAllForYouSg(scrapy.Spider):
    name = 'www_allforyou_sg_crawler'
    allowed_domains = ['allforyou.sg']
    start_urls = ['https://allforyou.sg/']

    def parse(self,response):
        for x in response.css("div.span2.categorybox-span > div.categorybox > div.thumb > a::attr('href')"):
            url = response.urljoin(x.extract())
            print "*******************************"
            print url
            yield scrapy.Request(url, callback=self.parse_subcategories)

    def parse_subcategories(self, response):
        #print "+++++++++++++++++++++++++++++++"
        #print response 
        for x in response.css("div.FeaturedHeader > h2 > a::attr('href')"):
            url = response.urljoin(x.extract())
            #print url
            yield scrapy.Request(url, callback=self.parse_pagination)

    def parse_pagination(self,response):
        print "*******************************"
        ctr = 1
        for x in response.css("div.pager > a.individual-page::text"):
            if x.extract()> ctr: ctr = x.extract()
        #print ctr
            #print ctr
            #print "pagination "
            #yield scrapy.Request(url, callback=self.parse_products)
        for y in range(1,int(ctr)+1):
            #print y
            url = response.urljoin('?pagenumber=%d'%y)
            #url = response.urljoin('')
            #print "pagination 1"
            #print url
            yield scrapy.Request(url, callback=self.parse_products)

    def parse_products(self, response):
        item = AllforyouItem()
        cat = ''
        cat = response.xpath('//title/text()').extract()[0] 
        for sel in response.xpath("//div/div[contains(@class,'prod-data')]"):
            item['_url'] = response.urljoin('')
            item['_offer'] = sel.xpath('@data-offername').extract()
            item['_description'] = sel.xpath('@data-desc').extract()
            item['_primary_img_url'] = sel.xpath('@data-imgurl').extract()
            item['_price'] = sel.xpath('@data-price').extract()
            item['_out_of_stock'] = sel.xpath('@data-outofstock').extract()
            item['_categories'] = cat[10:]
            item['_title'] = sel.xpath('@data-name').extract()
            item['_retailer_sku'] = sel.xpath('@id').extract()
            item['_crawlTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            yield item