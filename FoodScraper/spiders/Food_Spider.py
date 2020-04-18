import scrapy

from ..items import FoodscraperItem
from urllib.parse import urlparse, urljoin
from urllib.parse import parse_qs


class FoodSpider(scrapy.Spider):
    name = "food"
    start_urls = [
        'https://www.eatthismuch.com/food/browse/'
    ]

    baseUrl = "https://www.eatthismuch.com/"

    # recipes
    groups = {'Appetizers' : 20, 'Breakfast foods' : 43, 'Desserts' : 13, 'Drinks' : 10, 'Mostly meat' : 36, 'Salads' : 30, 'Sandwiches' : 15, 'Pasta' : 17,
              'Soups' : 15, 'Main dishes' : 88}

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

            item = FoodscraperItem()

            item['name'] = result.css(".result_name::text").extract()
            item['calories'] = result.css(".offset-1::text").extract()
            item['protein'] = result.css(".nutrient_cell:nth-child(4)::text").extract()
            item['fat'] = result.css(".nutrient_cell:nth-child(3)::text").extract()
            item['sugar'] = result.css(".col-3.nutrient_cell::text").extract()
            item['carb'] = result.css(".offset-1+ .nutrient_cell::text").extract()
            item['type'] = tp

            yield item
