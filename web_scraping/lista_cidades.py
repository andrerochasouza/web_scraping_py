import requests as req
from bs4 import BeautifulSoup as bs

def lista_cidade_principais():
    html_clima = req.get('https://www.climatempo.com.br/previsao-do-tempo?page=HOJE')
    html_clima_soup = bs(html_clima.text, 'html.parser')

    principais_cidade = []
    for cidade in html_clima_soup.find_all('div', {'class': 'featured-city-card card'}):
        principais_cidade.append(cidade.find('h2').text.split(','))
        principais_cidade[-1][-1] = principais_cidade[-1][-1].strip()

    return principais_cidade

def lista_climas_principais():
    html_clima = req.get('https://www.climatempo.com.br/previsao-do-tempo?page=HOJE')
    html_clima_soup = bs(html_clima.text, 'html.parser')

    principais_clima = []
    for clima in html_clima_soup.find_all('div', {'class': 'featured-city-card-temp'}):
        principais_clima.append(clima.find('span').text)

    return principais_clima

print(lista_cidade_principais())
print(lista_climas_principais())
