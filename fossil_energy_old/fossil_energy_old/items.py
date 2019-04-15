# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FossilEnergyOldItem(scrapy.Item):
    period = scrapy.Field() # Month and year
    coal = scrapy.Field() # Includes anthracite, bituminous, subbituminous, lignite, and waste coal; synthetic coal and refined coal; and coal-derived synthesis gas
    petro_liquids = scrapy.Field() # Includes distillate and residual fuel oils, jet fuel, kerosene, waste oil and propane
    petro_coke = scrapy.Field() # Includes petroleum coke-derived synthesis gas
    natural_gas = scrapy.Field()
    other_gas = scrapy.Field() # Includes blast furnace gas and other manufactured and waste gases derived from fossil fuels
    nuclear = scrapy.Field()