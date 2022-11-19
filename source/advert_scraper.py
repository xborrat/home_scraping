import requests
from bs4 import BeautifulSoup
import re
import csv
from datetime import datetime
import time


def data_extract(links_file):
    """Funció que obre totes les urls (urls dels anuncis de les cases) de urls.txt i n'extreu
     l'informació desitjada i l'afageix al data frame de l'arxiu house_df.csv"""

    with open(links_file,'r') as f:
        links_list = f.readlines()
        f.close()

    with open('dataset/houses_to_sell_df.csv', 'a+', newline='') as csvfile:
        

        for link in links_list:

            # Definim l'user agent
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\
              */*;q=0.8",
                "Accept-Encoding": "gzip, deflate, sdch, br",
                "Accept-Language": "en-US,en;q=0.8",
                "Cache-Control": "no-cache",
                "dnt": "1",
                "Pragma": "no-cache",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                                 Chrome/107.0.0.0 Safari/537.36"
            }

            t0 = time.time()

            # importem la web de cada anunci de casa
            page = requests.get(link, headers=headers)

            # càlculem el temps que tarda en descarregar el contingut
            delay = time.time() - t0

            soup = BeautifulSoup(page.content, 'html.parser')

            # creem la llista on guardarem els valors a afegir al csv
            info = []

            # Trobem tots els scripts ja que allà trobarem informació que ens interessa
            all_scripts = soup.find_all('script')

            # fem un for per trobar el script CriteoDTO que és el que conté l'informació desitjada
            for script in all_scripts:
                if (re.search("CriteoDTO", script.text)):
                    try:
                        pr_id = re.findall('(codigoProducto: .[0-9a-zA-Z]*)', script.prettify())[0]  # get a list with all codigoproducto (Product_id)
                        ad_id = re.findall('(codigoAnuncio: .[0-9a-zA-Z]*.)', script.prettify())[0] #(Advert_id)
                        preu = re.findall('(precioProducto: .[0-9a-zA-Z]*.)', script.prettify())[0] #(price)
                        city = re.findall('(nomPobBuscador: .[0-9a-zA-Z]*.)', script.prettify())[0]  #(City_name)
                        nom_zona = re.findall('(nomZonaBuscador: .[_0-9a-zA-Z]*.)', script.prettify())[0] #(zone)
                        city_code = re.findall('(codPob: .[0-9a-zA-Z]*)', script.prettify())[0] #(City_code)
                        zone_code = re.findall('(codZona: .[0-9a-zA-Z]*)', script.prettify())[0] #(Zone_code)
                    except:
                        pass
                    break

            tag = soup.find_all('li', class_="feature")
            metres = "NA"
            hab = "NA"
            banys = "NA"

            # fem un for per comprovar que realment agafem els metres, les habitacions i els lavabos
            # i no un altre valor
            for item in tag:
                if(len(item) >= 2):
                    if(item.text.split()[1] == "m2"):
                        metres = item.text.split()[0] # (square_maters)
                    if (item.text.split()[1] == "hab."):
                        hab = item.text.split()[0] # (Bed_rooms)
                    if (item.text.split()[1] == "baño" or item.text.split()[1] == "baños"):
                        banys = item.text.split()[0]  # (Toilets)

            info.append(pr_id.split(":")[1])  # we do split to separate the value we want which is on index 1
            info.append(ad_id.split("\'")[1])
            info.append(preu.split("\'")[1])
            info.append(city.split("\'")[1])
            info.append(nom_zona.split("\'")[1])
            info.append(city_code.split(":")[1])
            info.append(zone_code.split(":")[1])
            info.append(metres)
            info.append(hab)
            info.append(banys)
            info.append(link.strip()) #(advert_url)
            info.append(datetime.now()) #(today's_date)

            housewriter = csv.writer(csvfile)
            # ho guardem en el csv
            housewriter.writerow(info)
            # fem un sleep de 5 vegades el delay per no saturar els servidors
            time.sleep(5*delay)

        csvfile.close()
