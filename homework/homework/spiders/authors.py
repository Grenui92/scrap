import scrapy


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "json_files/authors.json"}
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    async def parse(self, response):
        author_links = response.xpath('//div[@class="quote"]/span/small[@class="author"]/following-sibling::a')
        for author_link in author_links:
            yield response.follow(author_link, self.author_parse)

        new_link = response.xpath("//li[@class='next']/a/@href").get()
        if new_link:
            yield scrapy.Request(self.start_urls[0]+new_link)


    def author_parse(self, response):
        fullname = response.xpath("/html//div[@class='author-details']/h3[@class='author-title']/text()").get().strip()
        born_date = response.xpath("/html//div[@class='author-details']/p/span[@class='author-born-date']/text()").get()
        born_location = response.xpath("/html//div[@class='author-details']/p/span[@class='author-born-location']/text()").get()
        yield {
            "fullname": fullname,
            "born_date": born_date,
            "born_location": born_location,
            "description": f"Born {born_location}: {born_date}"

        }