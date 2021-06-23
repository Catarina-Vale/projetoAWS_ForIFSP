import json
import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):

    state = event["queryStringParameters"]["estado"]

    state_url = f"https://www.ibge.gov.br/cidades-e-estados/{state}.html"

    page = requests.get(state_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    indicadors = soup.select('.indicador')

    state_dict = {}
    for ind in indicadors:
        if "\xa0\xa0\xa0" in ind.select('.ind-value')[0].text:
            state_dict[ind.select('.ind-label')[0].text] = ind.select('.ind-value')[0].text[:-9]
        else:
            state_dict[ind.select('.ind-label')[0].text] = ind.select('.ind-value')[0].text

    state_dict["Sigla Estado"] = state

    return {
        "statusCode": 200,
        "body": json.dumps(state_dict)
    }
