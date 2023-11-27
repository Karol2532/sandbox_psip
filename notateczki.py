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
#from .dane import users_list

user = {"city":"Giżycko","name":"Karol","nick":"plutas","posts":731}


#zwrócić mapę z pinezką odnoszącą się do użytkownika podanego z klawiatury
def get_ss_map_of(user:str)->None:
    city = get_coordinate(user['city'])

    map = folium.Map(
        location=city,
        tiles="OpenStreetMap",
        zoom_start=15)

    folium.Marker(
        location=city,
        popup= f'Tu rządzi {user["name"]} z geoinformatyki 2023'
    ).add_to(map)

    map.save(f'Mapka{user["name"]}.html')



#zwróci mapę z wszystkimi użytownikami z danej listy (znajomych)
def get_map_of(users:list)->None:
    map = folium.Map(
        location=[52.3,21.0],
        tiles="OpenStreetMap",
        zoom_start=7)

    for item in users:
        folium.Marker(
        location=get_coordinate(city=item["city"]),
        popup= f'Użytkownik: {item["name"]} \n'
        f' Liczba postów: {item["posts"]}'
        ).add_to(map)

        map.save('Mapka.html')

from dane import users_list
get_map_of(users_list)

