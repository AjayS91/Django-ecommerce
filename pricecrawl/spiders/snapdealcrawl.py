from scrapy import log
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from pricecrawl.xpaths import *

from price_display.models import price_display
"""
The spider responsible for crawling snapdeal.com
"""
class SnapdealSpider(Spider):
  name = 'snapdeal'
  allowed_domains = ['snapdeal.com']
  start_urls = []
  item_name = ""
  """
    Initialises the start_urls based upon the input dates.
  """
  def __init__(self, *args, **kwargs):
    try:
      tup = kwargs.get('product').split()
      product_name = tup[0]
      for i in xrange(1,len(tup)):
	product_name+='+'+tup[i]
      self.item_name = product_name
      self.start_urls.append(START_URL_PREFIX_sd + product_name + START_URL_SUFFIX_sd)
    except Exception as e:
      print e

  """
    The main parser for getting responses from the list of
    start_urls.
  """
  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    urls = hxs.select(PRODUCT_LINK_sd).extract()
    yield Request(urls[0], self.get_details)

  def get_details(self,response):
    hxs = HtmlXPathSelector(response)
    products = hxs.select(PRODUCT_NAME_sd).extract()
    first_product_name = products[0]
    prices = hxs.select(PRODUCT_SELLER_PRICES_sd).extract()
    sellers = hxs.select(PRODUCT_SELLER_NAMES_sd).extract()
    for i in xrange(0,len(prices)):
      s = price_display(product_name = first_product_name, sellername=sellers[i], portalname="snapdeal", itemname=self.item_name, price=prices[i])
      s.save()