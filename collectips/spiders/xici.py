# _*_ coding: utf-8 _*_
import scrapy
from collectips.items import CollectipsItem

class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ('http://www.xicidaili.com',)


    def start_requests(self):
        reqs = []
        for i in range(1,3):
            url = 'http://www.xicidaili.com/nn/%s'%i
            head = {'HOST': 'www.xicidaili.com',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
                    'Referer': url}

            req = scrapy.Request(url,headers=head)
            reqs.append(req)

        return reqs

    def parse(self, response):
        ip_list = response.xpath('//table[@id="ip_list"]')
        trs = ip_list[0].xpath('tr')
        items = []
        for ip in trs[1:]:
            pre_item = CollectipsItem()
            pre_item['IP'] = ip.xpath('td[2]/text()')[0].extract()
            pre_item['PORT'] = ip.xpath('td[3]/text()')[0].extract()
            pre_item['POSITION'] = ip.xpath('string(td[4])')[0].extract().strip()
            pre_item['TYPE'] = ip.xpath('td[6]/text()')[0].extract()
            # pre_item['SPEED'] = ip.xpath('td[8]/div[@class="bar"]/@title').re('\d{0,2}\.\d{0,}')[0]
            pre_item['LAST_CHECK_TIME'] = ip.xpath('td[8]/text()')[0].extract()
            items.append(pre_item)
        return items
