from scrapy.spider import Spider
from scrapy.selector import Selector
import json
from price_display.models import price_display
class DmozSpider(Spider):
    name = "ebay"
    allowed_domains = ["www.ebay.in"]
    start_urls = []
    def __init__(self,item="",**kwargs):
	try:
	    tup =item.split()
	    product_name = tup[0]
	    for i in xrange(1,len(tup)):
		product_name+='+'+tup[i]
	    self.item_name = product_name
	    self.start_urls = ['http://svcs.ebay.in/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=AjaySing-e1fb-4acd-a186-6f2ffa17edb7&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords=%s'%item]
	except Exception as e:
	    print e
    def parse(self,response):
	jsonresponse = json.loads(response.body_as_unicode())
	#print jsonresponse
	#print 'len==%d'%len(jsonresponse["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"])
	for i in range(0,len(jsonresponse["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"])):
	    itemresponse=jsonresponse["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"][i]
	    #print "title = %s,Currency = %s Price = %s"%(itemresponse["title"][0],itemresponse["sellingStatus"][0]["currentPrice"][0]["@currencyId"],itemresponse["sellingStatus"][0]["currentPrice"][0]["__value__"])
	    title = itemresponse["title"][0]
	    Price = itemresponse["sellingStatus"][0]["currentPrice"][0]["__value__"]
	    s = price_display(product_name =title,sellername=" ", portalname="Ebay", itemname=self.item_name, price=Price)
	    s.save()
	    
