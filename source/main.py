import csv
from os.path import exists
import os
import url_collector as coll
import advert_scraper as scrp
import whois

pages_num = 50
header = ['Product_id', 'Advert_id', 'Price', 'City_Name', 'Zone', 'City_code', 'Zone_code', 'Square_meters', 'Bed_rooms', 'Toilets', "advert_url", "today's_date"]

# inspeccionem qui és el propietari de www.habitaclia.com
print(whois.whois('https://www.habitaclia.com'))

for i in range(pages_num):

   # Fem un for per passar per les diferents pàgines d'anuncis de cases a BCN
   url_bcn = "https://www.habitaclia.com/viviendas-barcelona-{}.htm".format(i)
   coll.page_link_collector(url_bcn)

if exists('dataset/houses_to_sell_df.csv') == False:

    with open('dataset/houses_to_sell_df.csv', 'w', newline='') as csvfile:
        housewriter = csv.writer(csvfile)
        housewriter.writerow(header)
        csvfile.close()

# cridem la funció per fer scrapping del contingut dels anuncis
scrp.data_extract('urls.txt')
# eliminem l'arxiu temporal urls.txt
os.remove('urls.txt')
