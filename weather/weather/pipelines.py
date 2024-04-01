# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WeatherPipeline:
    def process_item(self, item, spider):
        if item['place'] is not None:
            item['place'] = item['place'].replace('历史天气', '').strip()
        if item['high'] is not None:
            item['high'] = item['high'].split('℃')[0].strip()
        if item['low'] is not None:
            item['low'] = item['low'].split('℃')[0].strip()

        if item['wind_level'] is not None:
            item['wind_level'] = item['wind_level'].split('级')[0].strip()
            item['wind_level'] = item['wind_level'].replace('微风', '1').strip()
            item['wind_level'] = item['wind_level'].replace('小于3', '2').strip()
            item['wind_level'] = item['wind_level'].split('-')[0].strip()
        return item
