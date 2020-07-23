import scrapy

import json
from ..items import FoodscraperItem
from urllib.parse import urlparse, urljoin
from urllib.parse import parse_qs
from pprint import pprint


class FoodSpider(scrapy.Spider):
    name = "food"
    start_urls = [
        'https://www.eatthismuch.com/food/browse/'
    ]

    baseUrl = "https://www.eatthismuch.com/"
    api = "https://www.eatthismuch.com/api/v1/recipe/"
    # recipes
    groups = {'Appetizers' : 20, 'Breakfast foods' : 43, 'Desserts' : 13, 'Drinks' : 10, 'Mostly meat' : 36, 'Salads' : 30, 'Sandwiches' : 15, 'Pasta' : 17,
              'Soups' : 15, 'Main dishes' : 88}
    # testing
    # groups = {'Appetizers': 1, 'Breakfast foods' : 1}

    # Basic Foods
    # groups = {'Snacks': 7}
    ind = 0
    typee = 'recipe'

    def parse(self, response):


        for group in FoodSpider.groups:
            while 0 < FoodSpider.groups[group]:
                yield scrapy.FormRequest.from_response(response=response,
                                                    formdata={'q': '', 'type': 'recipe', 'group': group ,
                                                              'page': str(FoodSpider.groups[group]), 'show_nutrient' : 'sugar', 'nutrition_display' : ''},
                                                    callback=self.parse_items)
                FoodSpider.groups[group] -= 1



    def parse_items(self, response):

        url = urlparse(response.url)
        tp = parse_qs(url.query)["group"]


        food_results = response.css('.food_result')

        for result in food_results:

            # item = FoodscraperItem()

            # item['name'] = result.css(".result_name::text").extract()
            # item['calories'] = result.css(".offset-1::text").extract()
            # item['protein'] = result.css(".nutrient_cell:nth-child(4)::text").extract()
            # item['fat'] = result.css(".nutrient_cell:nth-child(3)::text").extract()
            # item['sugar'] = result.css(".col-3.nutrient_cell::text").extract()
            # item['carb'] = result.css(".offset-1+ .nutrient_cell::text").extract()
            # item['type'] = tp

            id = result.css(".big_favorite_food ::attr(data-id)").extract()

            urll = FoodSpider.api + str(id[0]) + "/"

            yield scrapy.Request(url = urll, callback=self.getDetails, meta={'type': tp})

    def getDetails(self, response):

        jsonObj = json.loads(response.text)

        item = FoodscraperItem()

        #info

        item['name'] = jsonObj["food_name"]
        item['type'] = response.meta.get('type')
        item['id'] = jsonObj['id']
        item['breakfast'] = jsonObj['breakfast']
        item['cookTime'] = jsonObj['cook_time']
        item['complexity'] = jsonObj['complexity']
        item['is_basic_food'] = jsonObj['is_basic_food']
        item['is_recipe'] = jsonObj['is_recipe']
        item['is_snack'] = jsonObj['is_snack']
        item['main_dish'] = jsonObj['main_dish']
        item['needs_blender'] = jsonObj['needs_blender']
        item['needs_grill'] = jsonObj['needs_grill']
        item['needs_food_processor'] = jsonObj['needs_food_processor']
        item['needs_microwave'] = jsonObj['needs_microwave']
        item['needs_oven'] = jsonObj['needs_oven']
        item['needs_stove'] = jsonObj['needs_stove']
        item['needs_toaster'] = jsonObj['needs_toaster']
        item['num_favorites'] = jsonObj['num_favorites']
        item['servings'] = jsonObj['number_servings']
        item['grams_per_serving'] = jsonObj['weights'][1]['grams']
        item['prep_day_before'] = jsonObj['prep_day_before']
        item['prep_time'] = jsonObj['prep_time']

        item['ingredients'] = []
        ingreds = jsonObj['ingredients']
        for i in range(len(ingreds)):
            item['ingredients'].append(ingreds[i]['food']['food_name'])

        #nutrition info

        item['calories'] = jsonObj['nutrition']['calories']
        item['proteins'] = jsonObj['nutrition']['proteins']
        item['fats'] = jsonObj['nutrition']['fats']
        item['sugar'] = jsonObj['nutrition']['sugar']
        item['carbs'] = jsonObj['nutrition']['carbs']
        item['calcium'] = jsonObj['nutrition']['calcium']
        item['fiber'] = jsonObj['nutrition']['fiber']
        item['iron'] = jsonObj['nutrition']['iron']
        item['potassium'] = jsonObj['nutrition']['potassium']
        item['saturated_fats'] = jsonObj['nutrition']['saturated_fats']

        print(jsonObj["food_name"])
        print("############")
        print(jsonObj['food_name'])

        yield item
