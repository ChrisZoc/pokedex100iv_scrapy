# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Pokemongo100IvPipeline(object):
    def process_item(self, item, spider):
        title = item['poke_iv'].split(" ")
        if int(title[2]) < 10:
            return item
        raise DropItem('El pokemon aparecio hace más de 10 minutos')
        return item


