# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from thu.items import ThuCourseItem

class ThuCourseSpider(scrapy.Spider):
    name = 'thu_course'
    allowed_domains = ['course.thu.edu.tw']
    start_urls = ['http://course.thu.edu.tw/view-dept/106/1/everything']

    def parse(self, response):
        domain = 'http://course.thu.edu.tw'
        res = BeautifulSoup(response.body)
        for dp in res.select('tr a'):
            dp_url = domain + dp['href']
            yield scrapy.Request(dp_url, self.dp_parse)

    def dp_parse(self, response):
        res = BeautifulSoup(response.body)
        courses = res.select('.aqua_table tbody tr')
        for c in courses:
            item = ThuCourseItem()
            item['id'] = c.select('td')[0].text.strip()
            item['name'] = c.select('td')[1].text.strip()
            item['credit'] = c.select('td')[2].text.strip()
            item['time'] = c.select('td')[3].text.strip()
            item['teacher'] = c.select('td')[4].text.strip()
            item['num'] = c.select('td')[5].text.strip()
            item['department'] = c.select('td')[6].select('a')[0].text.strip()
            item['note'] = c.select('td')[6].text.strip()
            yield item
            
