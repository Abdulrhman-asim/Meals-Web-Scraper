# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import re



class FoodscraperPipeline(object):

    def process_item(self, item, spider):

        patternDec = re.compile('\d+(\.\d{1,2})?')
        patternName = re.compile('[\sA-Za-z&‘’]+')


        item['calories'] = re.search(patternDec, str(item['calories'])).group(0)
        item['protein'] = re.search(patternDec, str(item['protein'])).group(0)
        item['fat'] = re.search(patternDec, str(item['fat'])).group(0)
        item['sugar'] = re.search(patternDec, str(item['sugar'])).group(0)
        item['carb'] = re.search(patternDec, str(item['carb'])).group(0)

        name = re.findall(patternName, str(item['name']))

        item['name']
        tmp = ''
        for match in name:
            match = match.strip()

            if len(match) > 1:
                tmp = tmp + ' ' + match
            elif match == 'a':
                tmp = tmp + ' ' + match

        j = 0
        i = 0
        while i < len(tmp):
            if tmp[i] == ' ':
                j = i + 1
                while j < len(tmp):
                    if tmp[j] != ' ':
                        break
                    j += 1
                tmp = tmp[0: i] + ' ' + tmp[j: len(tmp)]
            i += 1

        tmp = tmp[3: len(tmp)]
        item['name'] = tmp

        return item
