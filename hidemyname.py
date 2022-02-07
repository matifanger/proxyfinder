import json
import re
import urllib
from html.parser import HTMLParser
from urllib.parse import urljoin

from scrapy import Field, Item, Selector
from scrapy.http import FormRequest, HtmlResponse, Request
from scrapy.spiders import CrawlSpider

from requests import Session




class ProxyServersPro(Item):
    ip = Field()
    port = Field()
    country = Field()
    speed = Field()
    protocol = Field()
    anon = Field()
    lastcheck = Field()
    speed = Field()


class ProxyServers(CrawlSpider):
    name = "ProxyServersProCrawler"

    allowed_domains = ["hidemy.name"]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
    }
    start_url = [
        "https://hidemy.name/es/proxy-list/?maxtime=200&type=45&anon=4#list",
        "https://hidemy.name/es/proxy-list/?maxtime=200&type=45&anon=4&start=64#list",
        "https://hidemy.name/es/proxy-list/?maxtime=200&type=45&anon=4&start=128#list",
        "https://hidemy.name/es/proxy-list/?maxtime=200&type=45&anon=4&start=192#list",
        "https://hidemy.name/es/proxy-list/?maxtime=200&type=45&anon=4&start=256#list",
    ]

    def __init__(self):
        super(ProxyServers, self).__init__()

    def start_requests(self):
        for url in self.start_url:
            yield Request(url, callback=self.parse_companies, headers=self.headers)

    def parse_companies(self, response):
        table = response.xpath('//table[@class="proxy__t"]/tbody/tr')
        for data in table:
            ip = data.xpath("./td[1]/text()").extract_first()
            country = data.xpath("./td[3]/div/text()").extract_first()
            protocol = data.xpath("./td[5]/text()").extract_first()
            anon = data.xpath("./td[6]/text()").extract_first()
            port = data.xpath('./td[2]/text()').extract_first()

            item = ProxyServersPro()
            item["ip"] = ip
            item["country"] = country
            item["protocol"] = protocol
            item["anon"] = anon
            item["port"] = port
            yield item