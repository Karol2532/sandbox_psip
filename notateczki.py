from bs4 import BeautifulSoup
import requests
import folium

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

#for item in city:
    #print(get_coordinate(item))

#zwrócić mapę z pinezką odnoszącą się do użytkownika podanego z klawiatury
#
## RYSOWANIE MAPY
city = get_coordinate(city='Zamość')

map = folium.Map(
    location=[52.3,21.0],
    tiles="OpenStreetMap",
    zoom_start=7)


folium.Marker(
        location=city,
        popup='Geoinformatyka rządzi !').add_to(map)

map.save('Mapka.html')