import json
import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):

    state = event["queryStringParameters"]["estado"]
    city = event["queryStringParameters"]["cidade"]

    city_url = f"https://www.ibge.gov.br/cidades-e-estados/{state}/{city}.html"
    page = requests.get(city_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    indicadors = soup.select('.indicador')

    city_dict = {}
    for ind in indicadors:
        if "\xa0\xa0\xa0" in ind.select('.ind-value')[0].text:
            city_dict[ind.select('.ind-label')[0].text] = ind.select('.ind-value')[0].text[:-9]
        else:
            city_dict[ind.select('.ind-label')[0].text] = ind.select('.ind-value')[0].text

    city_dict["Sigla Estado"] = state

    return {
        "statusCode": 200,
        "body": json.dumps(city_dict)
    }
