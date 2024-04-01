# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    place = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    weather = scrapy.Field()
    wind = scrapy.Field()
    wind_level = scrapy.Field()
    date = scrapy.Field()
    pass
