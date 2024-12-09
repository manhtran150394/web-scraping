import scrapy

from ssvscarper.items import StirItem

class SsvspiderSpider(scrapy.Spider):
    name = "ssvspider"
    allowed_domains = ["salesnow.jp"]
    # corporateNumber = '1000000000000'
    # start_urls = ["https://salesnow.jp/db/industries/it"]
    # start_urls = ["https://salesnow.jp/db/_next/data/J0YMfFjxXB02pGn0szoCr/industries/it/prefectures/aichi/page/1.json"]
    # start_urls = ["https://salesnow.jp/db/_next/data/J0YMfFjxXB02pGn0szoCr/companies/7011001040548.json"]
    # start_urls = ["https://salesnow.jp/db/_next/data/J0YMfFjxXB02pGn0szoCr/companies/1000000000000.json"]

    def start_requests(self):
        # coperates:
        # urls = [
        #     "https://salesnow.jp/db/_next/data/J0YMfFjxXB02pGn0szoCr/companies/1000000000000.json",
        #     "https://salesnow.jp/db/_next/data/J0YMfFjxXB02pGn0szoCr/companies/1010401124973.json",
        #     "https://salesnow.jp/db/_next/data/J0YMfFjxXB02pGn0szoCr/companies/7011001040548.json",
        #     "https://salesnow.jp/db/_next/data/J0YMfFjxXB02pGn0szoCr/companies/3120001077023.json",
        # ]
        # coperateNumber = 1000000000000
        # maxCoperateNumber = 9999999999999

        coperateNumber = 7011001040548
        maxCoperateNumber =   7011001040549
        while coperateNumber <= maxCoperateNumber:
            url = "https://salesnow.jp/db/_next/data/J0YMfFjxXB02pGn0szoCr/companies/" + str(coperateNumber) + ".json"
            yield scrapy.Request(url=url, callback=self.parse, errback=self.errback_parse)
            coperateNumber += 1

        # for url in urls:

    def parse(self, response):
        if response.status != 200:
            return
        stirItem = StirItem()
        corporate = response.json()['pageProps']['companyResponse']['company']

        mainIndustry = corporate['industryDetail']['name']
        if mainIndustry != 'IT':
            return

        subIndustriesList = corporate['industrySubsDetail']
        subIndustriesText = ''
        for subIndustry in subIndustriesList:
            subIndustriesText += subIndustry['name'] + '、'  
        stirItem['subIndustry'] = subIndustriesText
        isOutOfBusiness = corporate['isOutOfBussiness']
        isOutOfBusinessText = ''
        if isOutOfBusiness:
            isOutOfBusinessText = '廃業や倒産している企業（合併による解散なども含む）です。'
        else:
            isOutOfBusinessText = ''
        businessTagsList = corporate['businessTags']
        businessTagsText = ''
        for businessTag in businessTagsList:
            businessTagsText += businessTag['name'] + '、' 
        technologiesList = corporate['technologies']
        technologiesText = ''
        for technology in technologiesList:
            technologiesText += technology['name'] + '、' 

        # yield stirItem
        yield {
            '企業名': corporate['name'],
            '都道府県': corporate['prefecture']['name'],
            '市内': corporate['city']['name'],
            'Homepage': corporate['url'],
            '上場': corporate['listingClassification'],
            '電話番号': corporate['phoneNumber'],
            '郵便番号': corporate['postalCode'],
            '住所': corporate['address'],
            '従業員数': corporate['employeeNumber'],
            '設立年月日': corporate['establishmentDate'],
            '事業内容': businessTagsText,
        }

    def errback_parse(self, failure):
        # log all failures
        # self.logger.error(repr(failure))
        # print(repr(failure))
        pass