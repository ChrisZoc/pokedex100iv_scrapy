# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Pokemongo100IvItem(scrapy.Item):
    # define the fields for your item here like:
    poke_number = scrapy.Field() #hidden-xs hidden-tiny col-xs-1 pokenumber
    poke_name   = scrapy.Field() #font-size:18px
    poke_iv   = scrapy.Field() #iv
    poke_cp   = scrapy.Field() #cp
    time_mess = scrapy.Field() #time_mess
