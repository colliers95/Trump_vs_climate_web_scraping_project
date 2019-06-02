# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class RenewableEnergyNewItem(scrapy.Item):
    period = scrapy.Field() # Month and year
    wind = scrapy.Field()
    solarpv_utility = scrapy.Field() # Utility scale solar photovoltaic
    solar_thermal = scrapy.Field()
    wood = scrapy.Field()# Includes wood/wood waste solids (paper pellets, railroad ties, utility poles, wood chips, bark etc.), wood waste liquids (red liquor, sludge wood, spent sulfite liquor), and black liquor
    landfill_gas = scrapy.Field()
    bmsw = scrapy.Field() # Biogenic municipal solid waste
    other_waste = scrapy.Field() # Includes sludge waste, agricultural byproducts, and other biomass solids, liquids and gases (including digester gases and methane)
    geothermal = scrapy.Field()
    hydro = scrapy.Field()
    solarpv_small = scrapy.Field()

