import scrapy

from ssvscarper.items import StirItem

class SsvspiderSpider(scrapy.Spider):
    name = "ssvspider"
    allowed_domains = ["salesnow.jp"]
    # start_urls = ["https://salesnow.jp/db/industries/it"]
    # start_urls = ["https://salesnow.jp/db/_next/data/J0YMfFjxXB02pGn0szoCr/industries/it/prefectures/aichi/page/1.json"]
    start_urls = ["https://salesnow.jp/db/_next/data/J0YMfFjxXB02pGn0szoCr/companies/7011001040548.json"]

    def parse(self, response):
        stirItem = StirItem()
        # corporates = response.json()['pageProps']['companies']['companies']
        # corporate = response.json()['pageProps']['companies']['companies']
        corporate = response.json()['pageProps']['companyResponse']['company']

        # for corporate in corporates:
            # if response.status
        #1
        stirItem['companyName'] = corporate['name']
        #2
        stirItem['mainIndustry'] = corporate['industryDetail']['name']
        #3
        subIndustriesList = corporate['industrySubsDetail']
        subIndustriesText = ''
        for subIndustry in subIndustriesList:
            subIndustriesText += subIndustry['name'] + '、'  
        stirItem['subIndustry'] = subIndustriesText
        #4
        stirItem['prefecture'] = corporate['prefecture']['name']
        #5
        stirItem['city'] = corporate['city']['name']
        #6
        isOutOfBusiness = corporate['isOutOfBussiness']
        if isOutOfBusiness:
            stirItem['isOutOfBussiness'] = '廃業や倒産している企業（合併による解散なども含む）です。'
        else:
            stirItem['isOutOfBussiness'] = ''
        #7
        stirItem['employeeNumber'] = corporate['employeeNumber']
        #8
        stirItem['address'] = corporate['address']
        #9
        stirItem['establishmentDate'] = corporate['establishmentDate']
        #10
        stirItem['listingClassification'] = corporate['listingClassification']
        #11
        stirItem['postalCode'] = corporate['postalCode']
        #12
        stirItem['url'] = corporate['url']
        #13
        stirItem['phoneNumber'] = corporate['phoneNumber']
        #14
        businessTagsList = corporate['businessTags']
        businessTagsText = ''
        for businessTag in businessTagsList:
            businessTagsText += businessTag['name'] + '、' 
        stirItem['businessTags'] = businessTagsText
        #15
        technologiesList = corporate['technologies']
        technologiesText = ''
        for technology in technologiesList:
            technologiesText += technology['name'] + '、' 
        stirItem['technologies'] = technologiesText

        # yield stirItem
        yield {
            '企業名': corporate['name'],
            '都道府県': corporate['prefecture']['name'],
            '市内': corporate['city']['name'],
            'Homepage': corporate['url'],
            '上場': corporate['listingClassification'],
            'Business status': corporate['isOutOfBussiness'],
            'phoneNumber': corporate['phoneNumber'],
            'postalCode': corporate['postalCode'],
            'address': corporate['address'],
            'employeeNumber': corporate['employeeNumber'],
            'establishmentDate': corporate['establishmentDate'],
            'industryDetail': corporate['industryDetail']['name'],
            'subIndustries': subIndustriesText,
            'businessTags': businessTagsText,
            'technologies': technologiesText,
        }
    