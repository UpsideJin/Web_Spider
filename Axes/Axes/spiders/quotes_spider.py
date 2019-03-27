import scrapy

class QuotesSpider(scrapy.Spider):
    name="quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        # 'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self,response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open (filename, 'wb') as f:
        #     f.write(response.body)
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').get(),
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page, callback=self.parse)
            yield response.follow(next_page, callback=self.parse)