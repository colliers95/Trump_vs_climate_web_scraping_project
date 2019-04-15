from scrapy import Spider
from fossil_energy_new.items import FossilEnergyNewItem
import re

class FossilEnergySpider(Spider):
    name = 'fossilEnergynew_spider'
    allowed_urls = ['https://www.eia.gov']
    start_urls = ['https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_1_01']

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
                coal = int(re.sub('[, \t]',"",rows[i].xpath('./td[2]/text()').extract_first()))
                petro_liquids = int(re.sub('[, \t]',"",rows[i].xpath('./td[3]/text()').extract_first()))
                petro_coke = int(re.sub('[, \t]',"",rows[i].xpath('./td[4]/text()').extract_first()))
                natural_gas = int(re.sub('[, \t]',"",rows[i].xpath('./td[5]/text()').extract_first()))
                other_gas = int(re.sub('[, \t]',"",rows[i].xpath('./td[6]/text()').extract_first()))
                nuclear = int(re.sub('[, \t]',"",rows[i].xpath('./td[7]/text()').extract_first()))

                # Append the correct year to the period (month)
                if i >=1 and i <=12:
                    period_year = "".join([period," " ,y4[0]])
                elif i ==14:
                    period_year = "".join([period," " ,y5[0]])

            # Make and yield an item
            item = FossilEnergyNewItem()
            item['period'] = period_year
            item['coal'] = coal
            item['petro_liquids'] = petro_liquids
            item['petro_coke'] = petro_coke
            item['natural_gas'] = natural_gas
            item['other_gas'] = other_gas
            item['nuclear'] = nuclear

            yield item

