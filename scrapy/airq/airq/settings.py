# Scrapy settings for airq project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'airq'

SPIDER_MODULES = ['airq.spiders']
NEWSPIDER_MODULE = 'airq.spiders'

ITEM_PIPELINES = {'airq.pipelines.SQL': 100}

# LOG_FILE = 'scrapy.log'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'airq (+http://www.yourdomain.com)'
