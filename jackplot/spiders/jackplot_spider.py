import scrapy
from scrapy.selector import Selector
from jackplot.items import JackplotItem

class JackplotSpider(scrapy.Spider):
    name = "jackplot"
    allowed_domains = ["ketqua.net"]
    start_urls = []
    url = "http://ketqua.net/xo-so-truyen-thong.php?ngay={}"
    for month in range(10):
        if month > 0:
            for num in range(31):
                if num > 1:
                    start_urls.append(url.format(num) + "-" + str(month) + "-2020")
    def parse(self, response):
        questions = Selector(response).xpath('//*[@id="rs_0_0"]')

        for question in questions:
            item = JackplotItem()

            item['result'] = question.xpath('//*[@id="rs_0_0"]').extract()[0]
            yield item
