import requests
from bs4 import BeautifulSoup

def scrap_country_info() -> dict:
    print(f'Recolhendo informacao do pais')
    country_url = f"https://www.ibge.gov.br/cidades-e-estados"
    page = requests.get(country_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    indicadors = soup.select('.indicador')

    country_dict = {}
    for ind in indicadors:
        if "\xa0\xa0\xa0" in ind.select('.ind-value')[0].text:
            country_dict[ind.select('.ind-label')[0].text.replace("ç", "c").replace("í", "i").replace("Í", "I").replace("ã", "a").replace("Á", "A").replace("á", "a")] = ind.select('.ind-value')[0].text[:-9].replace("ó","o")
        else:
            country_dict[ind.select('.ind-label')[0].text.replace("ç", "c").replace("í", "i").replace("Í", "I").replace("ã", "a").replace("Á", "A").replace("á", "a")] = ind.select('.ind-value')[0].text.replace("ó","o")

    return country_dict

def scrap_state_info(state: str) -> dict:
    print(f'Recolhendo informacao do estado {state}')
    state_url = f"https://www.ibge.gov.br/cidades-e-estados/{state}.html"
    page = requests.get(state_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    indicadors = soup.select('.indicador')

    state_dict = {}
    for ind in indicadors:
        if "\xa0\xa0\xa0" in ind.select('.ind-value')[0].text:
            state_dict[ind.select('.ind-label')[0].text.replace("ç", "c").replace("í", "i").replace("Í", "I").replace("ã", "a").replace("Á", "A").replace("á", "a")] = ind.select('.ind-value')[0].text[:-9].replace("ó","o")
        else:
            state_dict[ind.select('.ind-label')[0].text.replace("ç", "c").replace("í", "i").replace("Í", "I").replace("ã", "a").replace("Á", "A").replace("á", "a")] = ind.select('.ind-value')[0].text.replace("ó","o")

    state_dict["Sigla Estado"] = state
    return state_dict

def scrap_city_info(city: str, state: str) -> dict:
    print(f'Recolhendo informacao da cidade de {city}')
    city_url = f"https://www.ibge.gov.br/cidades-e-estados/{state}/{city}.html"
    page = requests.get(city_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    indicadors = soup.select('.indicador')

    city_dict = {}
    for ind in indicadors:
        if "\xa0\xa0\xa0" in ind.select('.ind-value')[0].text:
            city_dict[ind.select('.ind-label')[0].text.replace("ç", "c").replace("í", "i").replace("Í", "I").replace("ã", "a").replace("Á", "A").replace("á", "a")] = ind.select('.ind-value')[0].text[:-9].replace("ó","o")
        else:
            city_dict[ind.select('.ind-label')[0].text.replace("ç", "c").replace("í", "i").replace("Í", "I").replace("ã", "a").replace("Á", "A").replace("á", "a")] = ind.select('.ind-value')[0].text.replace("ó","o")

    # city_dict = {
    #     ind.select('.ind-label')[0].text: ind.select('.ind-value')[0].text.encode("unicode-escape").decode("unicode-escape")
    #     for ind in indicadors
    #     }


    city_dict["Sigla Estado"] = state

    return city_dict
    
    #return [(ind.select('.ind-label')[0].text, ind.select('.ind-value')[0].text) for ind in indicadors]

def test():
    payload = requests.get("localhost:3000/pais")
    json = payload.json()

    return json


print(scrap_city_info("campinas", "sp"))
#print(scrap_state_info('sp'))
#print(scrap_country_info())
#print(test())