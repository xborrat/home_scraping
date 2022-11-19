import requests
from bs4 import BeautifulSoup
import re


def page_link_collector(container_url:str):
   """Funció que recull tots els links d'una url i els afegeix a un arxiu desc.txt"""
   page = requests.get(container_url) # page es l'objecte on es guarda el get
   soup = BeautifulSoup(page.content, 'html.parser') # soup objecte on es guarda el contingut de la web
   
   with open('desc.txt','a+',encoding='utf-8') as f:
      for link in soup.find_all('article', class_="js-list-item list-item-container js-item-with-link gtmproductclick"): # filtrem article amb el subdiccionari class...
            f.write(link.get('data-href'))
            f.write('\n')
      f.close()


# Esborrat contingut de desc.txt si exitia previament
with open('desc.txt','w',encoding='utf-8') as z:
   z.close()


for i in range(3):
   url_bcn = "https://www.habitaclia.com/viviendas-barcelona-{}.htm".format(i)
   print(url_bcn)
   page_link_collector(url_bcn)


