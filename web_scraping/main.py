# utilizar web scraping para obter informações sobre o clima de uma cidade
import requests as req
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

html_clima = req.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/3477/brasilia-df')
html_clima_soup = bs(html_clima.text, 'html.parser')

for i in html_clima_soup.find_all('span', {'class': 'variable -bold -gray'}):
    print(i.text)

min_temp = html_clima_soup.find('span', {'id': 'min-temp-1'}).text
