# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StirItem(scrapy.Item):
    # define the fields for your item here like:
    companyName = scrapy.Field()
    prefecture = scrapy.Field()
    city = scrapy.Field()
    isOutOfBussiness = scrapy.Field()
    url = scrapy.Field()    
    phoneNumber = scrapy.Field()
    address = scrapy.Field()
    mainIndustry = scrapy.Field()
    subIndustry = scrapy.Field()
    employeeNumber = scrapy.Field()
    establishmentDate = scrapy.Field()
    listingClassification = scrapy.Field()
    postalCode = scrapy.Field()
    businessTags = scrapy.Field()
    technologies = scrapy.Field()
    