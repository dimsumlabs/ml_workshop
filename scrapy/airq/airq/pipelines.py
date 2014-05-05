# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from MySQLdb import connect
from scrapy import log

HOST = 'localhost'
USER = 'scrapy'
PASSWD = 'some_password'
DB = 'Scrapy'


class SQL(object):
    def open_spider(self, spider):
        self.dbcon = connect(host=HOST, 
                             user=USER, 
                             passwd=PASSWD,
                             db=DB)
        self.cursor = self.dbcon.cursor()

    def process_item(self, item, spider):
        self.cursor.execute("INSERT INTO AirQuality (station, timestamp, "
                "air_quality) VALUES (%s, %s, %s)", (item['station'], 
                                                     item['timestamp'],
                                                     item['air_quality']))
        return item

    def close_spider(self, spider):
        self.dbcon.commit()


