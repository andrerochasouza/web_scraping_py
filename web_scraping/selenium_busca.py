from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import lista_cidades as lc


chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#  abrir o chrome e digitar no search hello world
cidades = lc.lista_cidade_principais()
chrome.get('https://www.climatempo.com.br/previsao-do-tempo?page=HOJE')
chrome.find_element(By.ID, 'Hub_previsao_cidade_saopaulo').click()