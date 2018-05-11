# -*- coding: utf-8 -*-
import scrapy,urllib


class TtSpider(scrapy.Spider):
    name = 'tt'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        tr_list = response.xpath('//table[@class="tablelist"]//tr')[1:-1]
        for tr in tr_list:
            item = {}
            item['title'] = tr.xpath("./td[1]/a/text()").extract_first()
            item['href'] = tr.xpath("./td[1]/a/@href").extract_first()
            item['href'] = urllib.parse.urljoin(self.start_urls[0],item['href'])
            item['class'] = tr.xpath("./td[2]/text()").extract_first()
            item['needs'] = tr.xpath("./td[3]/text()").extract_first()
            item['city'] = tr.xpath("./td[4]/text()").extract_first()
            item['publish_date'] = tr.xpath("./td[5]/text()").extract_first()
            print(item)
            yield item

        next_page_url = response.xpath("//a[@id='next']/@href").extract_first()
        print(next_page_url)
        next_page_url = urllib.parse.urljoin(self.start_urls[0],next_page_url) if next_page_url != 'javascript:;' else None
        if next_page_url is not None:
            print(next_page_url)
            yield scrapy.Request(next_page_url,callback=self.parse)

