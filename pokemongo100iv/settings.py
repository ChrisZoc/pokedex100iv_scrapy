# -*- coding: utf-8 -*-
BOT_NAME = 'pokemongo100iv'
SPIDER_MODULES = ['pokemongo100iv.spiders']
NEWSPIDER_MODULE = 'pokemongo100iv.spiders'

CONCURRENT_REQUESTS = 10
DOWNLOAD_DELAY = 5
ITEM_PIPELINES = {
    'pokemongo100iv.pipelines.Pokemongo100IvPipeline': 1
}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "pokemon"
MONGODB_COLLECTION = "100iv"
