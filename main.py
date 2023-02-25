import asyncio

from scrapy.crawler import CrawlerProcess

from homework.homework.spiders.quotes import QuotesSpider
from homework.homework.spiders.authors import AuthorsSpider
from db_scr.json_files import load_quotes_from_file, load_authors_from_file

async def main():
    proces = CrawlerProcess()
    proces.crawl(QuotesSpider)
    proces.crawl(AuthorsSpider)

    proces.start()

    await load_authors_from_file()
    await load_quotes_from_file()

if __name__ == '__main__':
    asyncio.run(main())
