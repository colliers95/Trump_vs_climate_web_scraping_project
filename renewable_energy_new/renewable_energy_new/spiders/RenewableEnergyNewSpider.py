from scrapy import Spider
from renewable_energy_new.items import RenewableEnergyNewItem
import re

class RenewableEnergySpider(Spider):
    name = 'renewableEnergynew_spider'
    allowed_urls = ['https://www.eia.gov']
    start_urls = ['https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_1_01_a']

    def parse(self, response):
        # Pull the table content
        rows = response.xpath('//tbody//tr')[24:39]

        # Pull the years from the table which have their data broken out per-month
        year_text = rows.xpath('.//td[@class="l t sel-1 linecontent sel-19"]/text()').extract()
        y4, y5 = map(lambda x: re.findall('\d+',x), year_text) # Gets each relevant year as a string in a 1-element list

        for i in range(0, len(rows),1):
            # Check if the current row is a space row in the table
            if not rows[i].xpath('.//td[@class="l t sel-1 linecontent sel-19"]/@class').extract():

                # The table data comes out with big spaces, and the numbers have comma's in the middle which need to be subbed out
                # 
                period = re.sub('[, \t]',"",rows[i].xpath('./td[1]/text()').extract_first())
                wind = int(re.sub('[, \t]',"",rows[i].xpath('./td[2]/text()').extract_first()))
                solarpv_utility = int(re.sub('[, \t]',"",rows[i].xpath('./td[3]/text()').extract_first()))
                solar_thermal = int(re.sub('[, \t]',"",rows[i].xpath('./td[4]/text()').extract_first()))
                wood = int(re.sub('[, \t]',"",rows[i].xpath('./td[5]/text()').extract_first()))
                landfill_gas = int(re.sub('[, \t]',"",rows[i].xpath('./td[6]/text()').extract_first()))
                bmsw = int(re.sub('[, \t]',"",rows[i].xpath('./td[7]/text()').extract_first()))
                other_waste = int(re.sub('[, \t]',"",rows[i].xpath('./td[8]/text()').extract_first()))
                geothermal = int(re.sub('[, \t]',"",rows[i].xpath('./td[9]/text()').extract_first()))
                hydro = int(re.sub('[, \t]',"",rows[i].xpath('./td[10]/text()').extract_first()))
                solarpv_small = int(re.sub('[, \t]',"",rows[i].xpath('./td[12]/text()').extract_first()))

                # Append the correct year to the period (month)
                if i >=1 and i <=12:
                    period_year = "".join([period," " ,y4[0]])
                elif i ==14:
                    period_year = "".join([period," " ,y5[0]])

                # Make and yield an item
                item = RenewableEnergyNewItem()
                item['period'] = period_year
                item['wind'] = wind
                item['solarpv_utility'] = solarpv_utility
                item['solar_thermal'] = solar_thermal
                item['wood'] = wood
                item['landfill_gas'] = landfill_gas
                item['bmsw'] = bmsw
                item['other_waste'] = other_waste
                item['geothermal'] = geothermal
                item['hydro'] = hydro
                item['solarpv_small'] = solarpv_small

                yield item

