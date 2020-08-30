import scrapy
from scrapy.selector import Selector
from Maoyan.items import MaoyanItem


class MaoyanmovieSpider(scrapy.Spider):
    name = 'MaoyanMovie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        yield scrapy.Request(url='https://maoyan.com/films?showType=3', callback=self.parse1)

    def parse1(self, response):
        divtags = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')[:10]
        for atag in divtags:
            movie_url = 'https://maoyan.com'+ atag.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=movie_url, callback=self.parse2)

    def parse2(self, response):
        
        item = MaoyanItem()

        # 电影名称
        movie_name = Selector(response=response).xpath('//h1[@class="name"]/text()').extract_first()

        # 电影类别
        categories = []
        for category in Selector(response=response).xpath('//a[@class="text-link"]/text()').extract():
            categories.append(category.strip())
        movie_categories = '/'.join(categories)

        # 上映时间
        release_date = Selector(response=response).xpath('//li[@class="ellipsis"][3]/text()').extract_first()[:10]

        item['movie_name'] = movie_name
        item['movie_categories'] = movie_categories
        item['release_date'] = release_date
        return item
