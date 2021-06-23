import json
import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):

    country_url = f"https://www.ibge.gov.br/cidades-e-estados"
    page = requests.get(country_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    indicadors = soup.select('.indicador')

    country_dict = {}
    for ind in indicadors:
        if "\xa0\xa0\xa0" in ind.select('.ind-value')[0].text:
            country_dict[ind.select('.ind-label')[0].text] = ind.select('.ind-value')[0].text[:-9]
        else:
            country_dict[ind.select('.ind-label')[0].text] = ind.select('.ind-value')[0].text

    
    return {
        "statusCode": 200,
        "body": json.dumps(country_dict)
    }
