from bs4 import BeautifulSoup
import requests

city = 'Olsztyn', 'Giżycko', 'Kolno'

def get_coordinate(city:str)-> list[float,float]:

    # pobranie strony internetowej
    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'

    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text, 'html.parser')

    # pobranie współrzędnych z strony internetowej
    response_html_latitude = response_html.select('.latitude')[1].text # . bo class
    response_html_latitude = float(response_html_latitude.replace(',','.'))
    response_html_longitude = response_html.select('.longitude')[1].text # . bo class
    response_html_longitude = float(response_html_longitude.replace(',','.'))

    return [response_html_latitude, response_html_longitude]

for item in city:
    print(get_coordinate(item))