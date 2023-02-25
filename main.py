import asyncio
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from homework.homework.spiders.quotes import QuotesSpider
from homework.homework.spiders.authors import AuthorsSpider



if __name__ == '__main__':
    proces = CrawlerProcess()

    proces.crawl(QuotesSpider)

    proces.crawl(AuthorsSpider)
    proces.start()
