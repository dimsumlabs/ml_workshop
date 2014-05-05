from dateutil.parser import parse

from scrapy import log # This module is useful for printing out debug information
from scrapy.spider import Spider
from scrapy.selector import Selector

from airq.items import AirqItem


class AirqSpider(Spider):
    name = 'air_quality'
    allowed_domains = ['aqhi.gov.hk']
    start_urls = [
            'http://www.aqhi.gov.hk/en.html',
    ]

    def parse(self, response):
        sel = Selector(response)
        stations = sel.xpath('//td[@class="tblCurrAQHI_tdName"]/a/text()')\
                .extract()
        values = [int(x) for x in 
                  sel.xpath('//td[@class="tblCurrAQHI_tdBand notSurrogate"'
                      ']/text()').extract()
                 if x.isdigit()]   
        t = sel.xpath('//tr[@class="tblCurrAQHI_trHeader"]/td/text()'
                ).extract()[0]
        timestamp = parse(t)

        items = []

        for s, v in zip(stations, values):
            item = AirqItem()
            item['station'] = s
            item['air_quality'] = v
            item['timestamp'] = timestamp
            items.append(item)
        
        self.log("Got {} items.".format(len(items)))

        return items
            

