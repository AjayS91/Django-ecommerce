"""
contains the xpaths and patterns used by the crawler.
"""
BASE_URL_fk = 'http://www.flipkart.com/'
START_URL_PREFIX_fk = 'http://www.flipkart.com/search?q='
START_URL_SUFFIX_fk = '&as=off&as-show=off&otracker=start'
PRODUCT_ID_fk = '//div[contains(@class, "product-unit")]/@data-pid'
PRODUCT_SELLER_PRICES_fk = '//span[contains(@class, "pxs-final-price")]/text()'
PRODUCT_SELLER_NAMES_fk = '//div[contains(@class, "seller-info")]/a/text()'
PRODUCT_NAME_fk = '//div[contains(@class,"lastUnit")]//div[contains(@class,"fk-font-big")]/text()'


BASE_URL_sd = 'http://www.snapdeal.com/'
START_URL_PREFIX_sd = 'http://www.snapdeal.com/search?keyword='
START_URL_SUFFIX_sd = '&santizedKeyword=&catId=&categoryId=&suggested=false&vertical=&noOfResults=20&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&url=&utmContent=&catalogID=&dealDetail='
PRODUCT_LINK_sd = '//a[contains(@class, "hit-ss-logger")]/@href'
PRODUCT_SELLER_PRICES_sd = '//div[contains(@class, "cont")]//strong[contains(@class, "redText")]/text()'
PRODUCT_SELLER_NAMES_sd = '//div[contains(@class, "cont")]//a[contains(@class, "mvLink")]/text()'
PRODUCT_NAME_sd = '//div[contains(@class,"pdpName")]/h1/text()'

#APP_ID_eb = 'MayankJh-4472-4bfd-bf21-eeef88a71d86'
#API_PRODUCT_INFO_eb = 'http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME='+APP_ID_eb+'&RESPONSE-DATA-FORMAT=XML&REST-PAYLOAD&keywords='

#for amazon
BASE_URL_az = 'http://www.amazon.in/'
START_URL_PREFIX_az = 'http://www.amazon.in/s/field-keywords='
PRODUCT_ID_az = '//div[contains(@id,"result_0")]/@name'
PRODUCT_SELLER_PRICES_az = '//div[contains(@class, "olpOffer")]//span[contains(@class, "olpOfferPrice")]/span/text()'
PRODUCT_SELLER_NAMES_az = '//p[contains(@class,"olpSellerName")]'
PRODUCT_SELLER_NAMES_az_2 = '//p[contains(@class,"olpSellerName")]//span/a/text()'
PAGE_NAVIGATOR_az = '//ul[contains(@class,"a-pagination")]/li/a/@href'
PRODUCT_NAME_az = '//div[contains(@id,"olpProductDetails")]//h1//text()'