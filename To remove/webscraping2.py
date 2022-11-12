import requests
from bs4 import BeautifulSoup
import re
import csv

url_hab = "https://www.habitaclia.com/"
url_bcn = "https://www.habitaclia.com/viviendas-barcelona.htm"
url_casa = "https://www.habitaclia.com/comprar-atico-en_venta_en_el_centro_de_esquerra_baixa_de_l_eixample-barcelona-i4737003814487.htm?f=&geo=p&from=list&lo=55"
url_casa2 = "https://www.habitaclia.com/comprar-piso-junto_a_la_l_illa_con_2_terrazas_piscina_y_jardines_les_corts-barcelona-i27066000000314.htm?pag=3&f=&geo=p&from=list&lo=55"

header = ['Product_id', 'Advert_id', 'Price', 'City_Name', 'Zone', 'City_code', 'Zone_code', 'Square_meters', 'Bed_rooms', 'Toilets', "advert_url", "today's_date"]

# creem el file on guardarem les dades

"""with open('house.csv', 'w', newline='') as csvfile:
    housewriter = csv.writer(csvfile)
    csvfile.close()"""

# importem la web de la casa en concret
page = requests.get(url_casa) # page es l'objecte on es guarda el get
soup = BeautifulSoup(page.content, 'html.parser') # soup objecte on es guarda el contingut de la web

# per si volem guardar la web en un arxiu
"""
with open('casa.html', 'w', encoding='utf-8') as f: # això per si volem guardar el contingut en un arxiu#
   f.write(str(soup.prettify())) # prettify transforma el contingut a eestructura imbrincada
"""

# busquem el script amb les variables que ens interessen
all_scripts = soup.find_all('script')[27] # de tota la web ens troba els scripts però a nos nomes ens interessa el 27 que es on hi ha la info que volem

# creem la llsita amb les variables de la casa
info = []
pr_id = re.findall('(codigoProducto: .[0-9a-zA-Z]*)',all_scripts.prettify())[0] # get a list with all codigoproducto (Product_id)
ad_id = re.findall('(codigoAnuncio: .[0-9a-zA-Z]*.)',all_scripts.prettify())[0] # get a list with all codigoAnuncio (Advert_id)
preu = re.findall('(precioProducto: .[0-9a-zA-Z]*.)',all_scripts.prettify())[0] # get a lis with all precidoProducto (price)
city = re.findall('(nomPobBuscador: .[0-9a-zA-Z]*.)',all_scripts.prettify())[0] # same with city
nom_zona = re.findall('(nomZonaBuscador: .[_0-9a-zA-Z]*.)',all_scripts.prettify())[0] # get a list with all nomZonaBuscador (zone)
city_code = re.findall('(codPob: .[0-9a-zA-Z]*)',all_scripts.prettify())[0]
zone_code = re.findall('(codZona: .[0-9a-zA-Z]*)',all_scripts.prettify())[0]


tag = soup.find_all('li', class_="feature")

metres = tag[0].text.split()[0] # metres quadrats (square_maters)
hab = tag[1].text.split()[0] # num habitacions (Bed_rooms)
banys = tag[2].text.split()[0] # num banys (Toilets

info.append(pr_id.split(":")[1]) # we do split to separate the value we want which is on index 1
info.append(ad_id.split("\'")[1])
info.append(preu.split("\'")[1])
info.append(city.split("\'")[1])
info.append(nom_zona.split("\'")[1])
info.append(city_code.split(":")[1])
info.append(zone_code.split(":")[1])
info.append(metres)
info.append(hab)
info.append(banys)


# ho guardem en el csv

with open('house.csv', 'a', newline='') as csvfile: # hcange w to a to overwrite
    housewriter = csv.writer(csvfile)
    housewriter.writerow(info)


