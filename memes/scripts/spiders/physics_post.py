import scrapy
import json

class PhysicsSpider(scrapy.Spider):
    name = "physics_post"

    def start_requests(self):

        with open('physics.json') as json_file:
            urls = json.load(json_file)

            for url in urls:
                yield scrapy.Request(url='http://old.reddit.com'+url['post_link'], callback=self.parse)

    def parse(self, response):
        post = response.css(".link")

        if post.css('a.title::attr(href)').get()[:5] == 'https':
            yield {
                'points': post.css('div.score::text').get(),
                'title': post.css('a.title::text').get(),
                'download_link': post.css('a.title::attr(href)').get()
            }