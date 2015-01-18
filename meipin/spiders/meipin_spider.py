# -*- coding: utf-8 -*-

import scrapy 
from scrapy.http import Request
from meipin.items import MeipinItem 
import re
from scrapy.http import Request,FormRequest


from urlparse import urljoin

from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

class MeipinSpider(CrawlSpider):
    name = 'meipin'
    start_urls = [
        "http://meipintu.com/",
    ]
    rules = (
        Rule(SgmlLinkExtractor(allow=(r'http://meipintu.com/index\?idx=\d+')), callback='parse_meipin',follow=True),
        #Rule(SgmlLinkExtractor(allow=(r'http://meipintu.com/more\?t=\d+\.\d+')), callback='parse_meipin',follow=True),
    )
    """
        return [FormRequest(url="http://meipintu.com/",
                    formdata={'more?t=0.11891555786132812'},
                    callback=self.after_post)]
    """

    
    def parse_meipin(self,response):
        item = MeipinItem()   
        item['title'] = response.css("div.item_info.fn_right h3 a::text").extract()
        item['pic'] = response.css("div.item_img.fn_left img::attr(src)").extract()
        return item 
