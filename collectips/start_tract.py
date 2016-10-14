#coding=utf8
# from asyncore import dispatcher
#
# from twisted.internet import reactor
# from scrapy.crawler import Crawler, CrawlerProcess
# from scrapy import log, signals
# from scrapy.utils.project import get_project_settings
# from spiders.xici import XiciSpider
#
# spider = XiciSpider()  #这里改为你的爬虫类名
# # dispatcher.connect(stop_reactor, signal=signals.spider_closed)
# settings = get_project_settings()
# crawler = CrawlerProcess(settings)
# # crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
# # crawler.configure()
# crawler.crawl(spider)
# crawler.start()
# log.start()
# reactor.run()

from scrapy.cmdline import execute

# scrapy_spider為剛剛建立的spider name，可以在這裡切換不同的spider

execute(['scrapy', 'crawl', 'xici'])