import scrapy


class PhysicsSpider(scrapy.Spider):
    name = "physics"

    def start_requests(self):
        urls = [
            'http://old.reddit.com/r/physicsmemes/',
        ]

        yield scrapy.Request(url=urls[0], callback=self.parse_main_page)

    def parse_main_page(self, response):
        posts = response.css(".link")
        for p in posts:
            next_page = p.css('a::attr(href)').get()
            yield({'post_link': next_page})