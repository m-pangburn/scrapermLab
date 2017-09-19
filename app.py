# -*- coding: utf-8 -*-

# app.py (v1)

"""Script to crawl Top Posts across sub reddits and store results in MongoDB
"""

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from reddit.spiders.post import PostSpider

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())

    process.crawl(PostSpider)
    process.start() # the script will block here until the crawling is finished
    