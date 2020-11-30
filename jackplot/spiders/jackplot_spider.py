import scrapy
from scrapy.selector import Selector
from jackplot.items import JackplotItem

class JackplotSpider(scrapy.Spider):
    name = "jackplot"
    allowed_domains = ["https://dantri.com.vn/"]
    start_urls = []
    url = "https://dantri.com.vn/suc-manh-so/phan-mem-bao-mat/trang-{}.htm"
    for num in range(30):
        if num > 0:
            start_urls.append(url.format(num))
    def parse(self, response):
        questions = Selector(response).xpath('.//ul[@class="dt-list dt-list--lg"]/li/div[@class="news-item news-item--timeline news-item--left2right"]/div[@class="news-item__content"]')

        for question in questions:
            item = JackplotItem()

            item['title'] = question.xpath('h3/a/text()').extract_first() 
            item['body'] = question.xpath('a/text()').extract_first()
            item['date'] = question.xpath('div[@class="news-item__meta"]/span/text()').extract_first() 
            yield item
