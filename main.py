import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrap_country_info() -> dict:
    print(f'Recolhendo informacao do pais')
    country_url = f"https://www.ibge.gov.br/cidades-e-estados"
    page = requests.get(country_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    indicadors = soup.select('.indicador')

    country_dict = {
        ind.select('.ind-label')[0].text: ind.select('.ind-value')[0].text
        for ind in indicadors
        }

    return country_dict

def scrap_state_info(state: str) -> dict:
    print(f'Recolhendo informacao do estado {state}')
    state_url = f"https://www.ibge.gov.br/cidades-e-estados/{state}.html"
    page = requests.get(state_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    indicadors = soup.select('.indicador')

    state_dict = {
        ind.select('.ind-label')[0].text: ind.select('.ind-value')[0].text
        for ind in indicadors
        }

    state_dict["Sigla-Estado"] = state
    return state_dict

def scrap_city_info(city: str, state: str) -> dict:
    print(f'Recolhendo informacao da cidade de {city}')
    city_url = f"https://www.ibge.gov.br/cidades-e-estados/{state}/{city}.html"
    page = requests.get(city_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    indicadors = soup.select('.indicador')

    city_dict = {
        ind.select('.ind-label')[0].text: ind.select('.ind-value')[0].text[:-9]
        for ind in indicadors
        }

    city_dict["Sigla-Estado"] = state

    return city_dict
    
    #return [(ind.select('.ind-label')[0].text, ind.select('.ind-value')[0].text) for ind in indicadors]



#print(scrap_city_info("curitiba", "pr"))
#print(scrap_state_info('sp'))
#print(scrap_country_info())