import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "json_files/quotes.json"}
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    async def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            yield {
                "tags": quote.xpath("div[@class='tags']/a/text()").extract(),
                "author": quote.xpath("span/small[@class='author']/text()").get(),
                "quote": quote.xpath("span[@class='text']/text()").get()
            }
            new_link = response.xpath("//li[@class='next']/a/@href").get()
            if new_link:
                yield scrapy.Request(self.start_urls[0] + new_link)