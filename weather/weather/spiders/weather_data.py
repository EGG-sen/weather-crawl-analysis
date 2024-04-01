import scrapy

from weather.items import WeatherItem


class WeatherDataSpider(scrapy.Spider):
    name = "weather_data"
    allowed_domains = ["m.tianqi.com"]
    # start_urls = ["https://m.tianqi.com/lishi/zhangzhou/202304.html", "https://m.tianqi.com/lishi/quanzhou/202304.html",
    #               "https://m.tianqi.com/lishi/xiamen/202304.html"]
    start_urls = ["https://m.tianqi.com/lishi"]

    # 历史数据页
    def detail_parse_data(self, response):
        item = response.meta['weather_item']
        item['date'] = response.xpath(
            ".//div[@class='alioq']/a[@class='listto']/div[@class='wi190']/span[1]/text()").get()
        item['high'] = response.xpath(
            ".//a[@class='listto']/div[@class='wi140 flex_cen'][1]/text()").get()
        item['low'] = response.xpath(
            ".//a[@class='listto']/div[@class='wi140 flex_cen'][2]/text()").get()
        item['weather'] = response.xpath(
            ".//a[@class='listto']/div[@class='wi140 flex_cen'][3]/text()").get()
        item['wind'] = response.xpath(
            ".//a[@class='listto']/div[@class='wi140 flex_cen'][4]/span[1]/text()").get()
        item['wind_level'] = response.xpath(
            ".//a[@class='listto']/div[@class='wi140 flex_cen'][4]/span[2]/text()").get()
        yield item

    # 具体城市
    def detail_parse2(self, response):
        for i in response.xpath("//div[@class='hist']"):
            weather_item = WeatherItem()
            weather_item['place'] = response.xpath(".//header[@class='header2']/h3/text()").get()
            url = i.xpath(".//div/a[@class='diandian']/@href").getall()
            for j in range(len(url)):
                next_url = "https://m.tianqi.com" + url[j]
                yield scrapy.Request(url=next_url, callback=self.detail_parse_data, meta={'weather_item': weather_item},
                                     dont_filter=True)

    # 省份城市页面
    def detail_parse1(self, response):
        for i in response.xpath("//div[@class='newSearchList']"):
            url = i.xpath(".//div[@class='newSearchList_box clear']/ul[@class='clear']/li/a/@href").getall()
            for j in range(len(url)):
                next_url = "https://m.tianqi.com" + url[j]
                yield scrapy.Request(url=next_url, callback=self.detail_parse2, dont_filter=True)

    # 主页面
    def parse(self, response):
        for i in response.xpath("//div[@class='newProvince'][1]/ul[@class='clear']"):
            url = i.xpath(".//li[7]/a/@href").getall()
            for j in range(len(url)):
                next_url = "https://m.tianqi.com" + url[j]
                yield scrapy.Request(url=next_url, callback=self.detail_parse1, dont_filter=True)
