# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ThuCourseItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    credit = scrapy.Field()
    time = scrapy.Field()
    teacher = scrapy.Field()
    num = scrapy.Field()
    department = scrapy.Field()
    note = scrapy.Field()
