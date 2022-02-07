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

    allowed_domains = ["proxydb.net"]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
    }
    start_url = [
        "http://proxydb.net/?protocol=socks5&anonlvl=4&min_uptime=75&max_response_time=5&country=",
    ]

    def __init__(self):
        super(ProxyServers, self).__init__()

    def start_requests(self):
        for url in self.start_url:
            yield Request(url, callback=self.parse_companies, headers=self.headers)

    def parse_companies(self, response):
        table = response.xpath('//table[@class="table table-sm table-hover"]/tbody/tr')
        for data in table:
            ip = data.xpath("./td[1]/*").extract_first()
            country = data.xpath("./td[3]/abbr/text()").extract_first()
            protocol = data.xpath("./td[5]/text()").extract_first()
            anon = data.xpath("./td[6]/span/text()").extract_first()

            item = ProxyServersPro()
            item["ip"] = ip
            item["country"] = country
            item["protocol"] = protocol
            item["anon"] = anon
            yield item