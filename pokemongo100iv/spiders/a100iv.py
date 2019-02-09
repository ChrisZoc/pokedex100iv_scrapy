# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
import scrapy
from pokemongo100iv.items import Pokemongo100IvItem
from scrapy.selector import Selector
#from itertools import izip, count

class A100ivSpider(CrawlSpider):
    name = '100iv'
    allowed_domains = ['pokedex100.com']
    start_urls = ['https://pokedex100.com/']

    def parse(self, response):
        items = []
        selector = Selector(response)
        poke_numbers = selector.xpath('//td[@class="hidden-xs hidden-tiny col-xs-1 pokenumber"]/text()').extract()
        poke_names = selector.xpath('//strong[@style="font-size:18px"]/text()').extract()
        poke_ivs = selector.xpath('//td[@class="iv"]/text()').extract()
        poke_cps = selector.xpath('//td[@class="cp"]/text()').extract()
        time_messes = selector.xpath('//td[@class="time_mess"]/text()').extract()

        for poke_number,poke_name,poke_iv,poke_cp,time_mess in zip(poke_numbers,poke_names,poke_ivs,poke_cps,time_messes):

            item = Pokemongo100IvItem()
            
            item['poke_number'] = poke_number
            item['poke_name'] = poke_name
            item['poke_iv'] = poke_iv
            item['poke_cp'] = poke_cp
            item['time_mess'] = poke_mess

            items.append(item)
        return items
