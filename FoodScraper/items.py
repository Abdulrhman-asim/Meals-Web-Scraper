# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FoodscraperItem(scrapy.Item):
    # define the fields for your item here like:

    #nutrition per 100g

    calories = scrapy.Field()
    proteins = scrapy.Field()
    fats = scrapy.Field()
    sugar = scrapy.Field()
    carbs = scrapy.Field()
    calcium = scrapy.Field()
    fiber = scrapy.Field()
    iron = scrapy.Field()
    potassium = scrapy.Field()
    saturated_fats = scrapy.Field()


    #info

    name = scrapy.Field(serializer=str)
    type = scrapy.Field()
    breakfast = scrapy.Field()
    cookTime = scrapy.Field()
    complexity = scrapy.Field()
    id = scrapy.Field()
    is_basic_food = scrapy.Field()
    is_recipe = scrapy.Field()
    is_snack = scrapy.Field()
    main_dish = scrapy.Field()
    needs_blender = scrapy.Field()
    needs_grill = scrapy.Field()
    needs_food_processor = scrapy.Field()
    needs_microwave = scrapy.Field()
    needs_oven = scrapy.Field()
    needs_stove = scrapy.Field()
    needs_toaster = scrapy.Field()
    num_favorites = scrapy.Field()
    servings = scrapy.Field()
    grams_per_serving = scrapy.Field()
    prep_day_before = scrapy.Field()
    prep_time = scrapy.Field()
    ingredients = scrapy.Field()

