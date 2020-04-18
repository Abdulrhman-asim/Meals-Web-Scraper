# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FoodscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(serializer = str)
    type = scrapy.Field()
    calories = scrapy.Field()
    protein = scrapy.Field()
    fat = scrapy.Field()
    sugar = scrapy.Field()
    carb = scrapy.Field()

