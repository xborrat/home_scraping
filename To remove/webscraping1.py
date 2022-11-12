import requests
from bs4 import BeautifulSoup
import re

url_hab = "https://www.habitaclia.com/"
url_bcn = "https://www.habitaclia.com/viviendas-barcelona.htm"
url_casa = "https://www.habitaclia.com/comprar-atico-en_venta_en_el_centro_de_esquerra_baixa_de_l_eixample-barcelona-i4737003814487.htm?f=&geo=p&from=list&lo=55"

page = requests.get(url_bcn) # page es l'objecte on es guarda el get
soup = BeautifulSoup(page.content, 'html.parser') # soup objecte on es guarda el contingut de la web

"""
tag = soup.find('article') # es una diccionari, que la key son etiquetes. en aquest casa guardem el contingut de l-etiqueta article. Ojo que aixo nomes triar el primer que trova xk es find
print(tag) # així podem imprimir que hi ha dins d'article
print(tag.attrs) # amb .attrs podem trobar quins diccionaris hi han dins d'aquest diccionari (article). Això ens retorna les keys dels diccionaris interiors
tag = soup.find('a') # lo mateix dincs el diccionari a
print(tag.attrs)

"""


"""
print(soup.prettify())
with open('desc.txt', 'w', encoding='utf-8') as f: # això per si volem guardar el contingut en un arxiu#
   f.write(str(soup.prettify())) # prettify transforma el contingut a eestructura imbrincada
"""

for link in soup.find_all('article', class_="js-list-item list-item-container js-item-with-link gtmproductclick"): # filtrem article amb el subdiccionari class...
    print(link.get('data-href')) # dins de la key articles filtart per las class que volem obtenim la url que està guardada dins la key data-href
                                 # s'haura d'iterar perque nomes surten les de la pagina i hi han mes de 1000 pagines

