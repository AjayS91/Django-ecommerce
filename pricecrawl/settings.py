# Scrapy settings for pricecrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'pricecrawl'

SPIDER_MODULES = ['pricecrawl.spiders']
NEWSPIDER_MODULE = 'pricecrawl.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pricecrawl (+http://www.yourdomain.com)'
import sys
sys.path.append('/home/aj91/Internship/crawlcode')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'pricecrawl_web.settings'
