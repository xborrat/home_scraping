import requests
from bs4 import BeautifulSoup
import time


def page_link_collector(container_url:str):
   """Funció que recull tots els links d'una url i els afegeix a un arxiu urls.txt"""

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

   # importem la web amb els enllaços als anuncis que ens interessen.
   t0 = time.time()
   page = requests.get(container_url, headers=headers)
   # càlculem el temps que tarda en descarregar el contingut
   delay = time.time() - t0
   soup = BeautifulSoup(page.content, 'html.parser')
   
   with open('urls.txt','a+',encoding='utf-8') as f:

       # Fem un filtre a article (és on estan les urls dels anuncis que ens interessa) i fem un for per obtenir
       # les urls en sí i les guardem a urls.txt
      for link in soup.find_all('article', class_="js-list-item list-item-container js-item-with-link gtmproductclick"):
            f.write(link.get('data-href')) # obtenim les url dels anuncis que ens interessen
            f.write('\n')
      f.close()

   # fem un sleep de 5 vegades el delay per no saturar els servidors
   time.sleep(5*delay)


