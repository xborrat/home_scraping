# Houses to sell
A  webscraping tool to explore the real-state pulse.

Autors:
Xavier Borrat
Roger Álvarez

Com executar Houses to sell:
1.	Assegurar-se que existeix el directori source/dataset ja que és allà on es guardarà el data set houses_to_sell_df.csv
2.	En l’arxiu main.py existeix una variable anomenada pages_num (línia 8) que per defecte te el valor de 50. Aquesta variable serveix per limitar el número de pàgines web on buscarem anuncis de pisos a Barcelona. A habitaclia hi ha més de 20.000 anuncis d’habitatges a Barcelona (unes 1350 pàgines amb anuncis de pisos), per tant si no posem un límit el temps d’execució seria enorme. Per defecte són 50 pàgines, que tot i així comporta un temps alt d’execució, per tant es recomana que abans d’executar el programa es redueixi aquest valor. Amb un valor de 10 es redueix el temps i ja es veu com funciona.
3.	Finalment només cal fer un run de main.py per executar i crear el data set.

Descripció d’arxius que composen el repositori:

1.	Archive: en aquesta carpeta s’han guardat esborranys inicials del codi i la memòria. La seva finalitat és purament de referència.
2.	Dataset: dins de la carpeta dataset podem trobar una còpia del data set creat houses_to_sell_df.csv.
3.	References: dins de la carpeta references trobarem les referències utilitzades. En aquest cas una còpia de l’anunciat de la pràctica.
4.	Source: dins de la carpeta source hi ha el codi del programa i la carpetadata set:
5.  source/Main.py: arxiu principal que executarà tot el programa.
6.  source/url_collector.py: codi de la funció que s’encarrega de descarregar els enllaços url dels anuncis de pisos.
7.  source/Advert_scraper.py: codi de la funció que s’encarrega de fer el scraping de cada anunci per obtenir les dades desitjades i les afegirà en el dataset.
8.  source/Dataset: dins aquesta carpeta és on es guardarà el data set houses_to_sell_df.csv. 
9.  LICENSE: llicència seleccionada. En el nostre cas una llicència Apache 2.0
10. Memòria.pdf: és la memòria de la pràctica.
11. Requirements.txt: arxiu que conté les llibreries necessàries per executar el codi. 



DOI de Zenodo:

DOI: 10.5281/zenodo.7338399

Video link:

https://drive.google.com/file/d/1Oc549dD_KJAgwC4HooybSW_RDbKZpwXn/view?usp=share_link


