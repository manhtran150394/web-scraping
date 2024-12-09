import scrapy
import csv

from ssvscarper.items import StirItem

def get_urls_from_csv():
    with open('CorporateNumberList.csv', 'r') as csv_file:
        data = csv.reader(csv_file)
        scrapurls = []
        for row in data:
            # url = "https://salesnow.jp/db/_next/data/ej1CMr-XFJsvEJFG9iKM6/companies/" + row[0] + ".json"
            url = "https://salesnow.jp/db/_next/data/cAhoZJzbkQD8AYPJ5HjYs/companies/" + row[0] + ".json"
            scrapurls.append(url)
        return scrapurls
    
class SsvspiderSpider(scrapy.Spider):
    name = "ssvspider"
    allowed_domains = ["salesnow.jp"]
    

    def start_requests(self):
        return [scrapy.http.Request(url=start_url) for start_url in get_urls_from_csv()]
    
        # coperateNumber = 7011001040548
        # maxCoperateNumber =   7011001040549
        # while coperateNumber <= maxCoperateNumber:
        #     url = "https://salesnow.jp/db/_next/data/J0YMfFjxXB02pGn0szoCr/companies/" + str(coperateNumber) + ".json"
        #     yield scrapy.Request(url=url, callback=self.parse, errback=self.errback_parse)
        #     coperateNumber += 1

        # for url in urls:

    def parse(self, response):
        # if response.status != 200:
        #     return
        stirItem = StirItem()
        corporate = response.json()['pageProps']['companyResponse']['company']

        mainIndustry = corporate['industryDetail']['name']
        # if mainIndustry != 'IT':
        #     return

        subIndustriesObj = corporate['industrySubsDetail']
        # print('1 ===========> ' + subIndustriesObj)
        subIndustriesList = []
        for subIndustry in subIndustriesObj:
            subIndustriesList.append(subIndustry['name'])
        #     subIndustriesText += subIndustry['name'] + '、'  
        # print('===========> ')
        # print(subIndustriesList)
        # return
        subIndustriesText = '、'.join(subIndustriesList)
        stirItem['subIndustry'] = subIndustriesText
        isOutOfBusiness = corporate['isOutOfBussiness']
        isOutOfBusinessText = ''
        if isOutOfBusiness:
            isOutOfBusinessText = '廃業や倒産している企業（合併による解散なども含む）です。'
        else:
            isOutOfBusinessText = ''
        businessTagsListObj = corporate['businessTags']
        businessTagsList = []
        for businessTag in businessTagsListObj:
            businessTagsList.append(businessTag['name'])
            # businessTagsText += businessTag['name'] + '、' 
        businessTagsText = '、'.join(businessTagsList)
        # technologiesList = corporate['technologies']
        # technologiesText = '、'.join(technologiesList)
        # for technology in technologiesList:
        #     technologiesText += technology['name'] + '、' 

        # yield stirItem
        yield {
            'Corp Num': corporate['corporateNumber'],
            '企業名': corporate['name'],
            '都道府県': corporate['prefecture']['name'],
            '市内': corporate['city']['name'],
            'Homepage': corporate['url'],
            'ステータス': isOutOfBusinessText,
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