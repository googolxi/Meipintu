# -*- coding: utf-8 -*-

# Scrapy settings for meipin project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'meipin'

SPIDER_MODULES = ['meipin.spiders']
NEWSPIDER_MODULE = 'meipin.spiders'
ITEM_PIPELINES = {
    'meipin.pipelines.MeipinPipeline': 1
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'meipin (+http://www.yourdomain.com)'
