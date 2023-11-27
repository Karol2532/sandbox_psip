from dane import users_list
from bs4 import BeautifulSoup
import requests
import folium
def add_user_to(users_list: list) -> None:
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('podaj imię')
    nick = input('podaj nick')
    posts = input('podaj liczbę postów')
    users_list.append({"name": name, "nick": nick, "posts": posts})

#add_user_to(users_list)

def remove_user_from(users_list: list) -> None:
    """
    remove object from list
    :param users_list: list - user list
    :return: None
    """
    tmp_list = []
    name = input('podaj imię użytkownika do usunięcia')
    for user in users_list:
        if user['name'] == name:
            tmp_list.append(user)
    print(f'Znaleziono użytkowników:')
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek+1}: {user_to_be_removed}')
    print('0: usuń wszystkich znalezionych użytkowników')
    numer = int(input(f'wybierz użytkownika do usunięcia:'))
    if numer == 0:
        for user in tmp_list:
            users_list.remove(user)
    else:
        users_list.remove(tmp_list[numer - 1])

def show_users_from(users_list: list)-> None:
    for user in users_list:
        print(f'Twój znajomy {user["name"]} dodał {user["posts"]} postów')

def update_user(users_list: list[dict,dict]) -> None:
    nick_of_user = input('Podaj nick użytkownika do modyfikacji: ')
    for user in users_list:
        if user['nick'] == nick_of_user:
            print('Znaleziono użytkownika')
            user['city'] = input('Podaj nowe miasto: ')
            user['name'] = input('Podaj nowe imię: ')
            user['nick'] = input('Podaj nową nick: ')
            user['posts'] = int(input('Podaj liczbę postów: '))

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

#zwrócić mapę z pinezką odnoszącą się do użytkownika podanego z klawiatury
def get_ss_map_of(user:str)->None:
    city = get_coordinate(user["city"])

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


def gui(users_list) -> None:
    while True:
        print(f'\nWitaj na WATbooku \n'
              f'0: Zamknij serwis \n'
              f'1: Wyświetl użytkowników \n'
              f'2: Dodaj użytkownika \n'
              f'3: Usuń użytkownika \n'
              f'4: Edytuj użytkownika \n'
              f'5: Lokalizacja pojedyńczego użytkownika \n'
              f'6: Mapa wszystkich użytkowników')

        menu_option = int(input('\nWybierz funkcję do wykonania '))
        print(f'Wybrano funkcję {menu_option}\n')

        match menu_option:
            case 0:
                print('Zamykam serwis')
                break
            case 1:
                print('Wyświetlanie listy użytkowników')
                show_users_from(users_list)
            case 2:
                print('Dodawanie użytkownika')
                add_user_to(users_list)
            case 3:
                print('Usuwanie użytkownika')
                remove_user_from(users_list)
            case 4:
                print('Edytowanie użytkownika')
                update_user(users_list)
            case 5:
               print('Tworzę mapę z lokalizacją użytkownika')
               user = input('Podaj nazwę użytkownika do zlokalizowania')
               for item in users_list:
                   if item["nick"] == user:
                       get_ss_map_of(item)
            case 6:
                print('Tworzę mapę wszystkich użytkowników')
                get_map_of(users_list)

