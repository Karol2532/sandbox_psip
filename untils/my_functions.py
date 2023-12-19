import psycopg2
from bs4 import BeautifulSoup
import requests
import folium

db_params = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='123',
    host='localhost',
    port=5433
)

cursor = db_params.cursor()


def add_user_to() -> None:
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('Podaj imię')
    nick = input('Podaj nick')
    posts = input('Podaj liczbę postów')
    city = input('Podaj miejscowość')
    sql_query_1 = f"INSERT INTO public.watbook(city, name, nick, posts) VALUES ('{city}', '{name}', '{nick}', '{posts}');"
    cursor.execute(sql_query_1)
    db_params.commit()


# add_user_to(users_list)

def remove_user_from() -> None:
    """
    remove object from list
    :param users_list: list - user list
    :return: None
    """

    name = input('Podaj imię użytkownika do usunięcia')
    sql_query_1 = f"SELECT * FROM public.watbook WHERE name ='{name}';"
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()
    print(f'Znaleziono użytkowników:')
    print('0: Usuń wszystkich znalezionych użytkowników')
    for numerek, user_to_be_removed in enumerate(query_result):
        print(f'{numerek + 1}: {user_to_be_removed}')
    numer = int(input(f'Wybierz użytkownika do usunięcia:'))
    if numer == 0:
        sql_query_2 = f"DELETE FROM public.watbook WHERE name ='{name}';"
        cursor.execute(sql_query_2)
        db_params.commit()
    else:
        sql_query_2 = f"DELETE FROM public.watbook WHERE id='{query_result[numerek - 1][0]}';"
        cursor.execute(sql_query_2)
        db_params.commit()


def show_users_from() -> None:
    sql_query_1 = f" SELECT * FROM public.watbook;"
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()
    for row in query_result:
        print(f'Twój znajomy {row[2]} dodał {row[4]} postów')


def update_user() -> None:
    nick_of_user = input('Podaj nick użytkownika do modyfikacji: ')
    sql_guery_1 = f"SELECT * FROM public.watbook WHERE nick= '{nick_of_user}';"
    cursor.execute(sql_guery_1)
    print('Znaleziono użytkownika')
    name = input('Podaj nowe imię: ')
    nick = input('Podaj nową nick: ')
    posts = int(input('Podaj liczbę postów: '))
    city = input('Podaj nowe miasto: ')
    sql_guery_2 = f"UPDATE public.watbook SET city='{city}', name='{name}', nick='{nick}', posts='{posts}' WHERE nick='{nick_of_user}';"
    cursor.execute(sql_guery_2)
    db_params.commit()


def get_coordinate(city: str) -> list[float, float]:
    # pobranie strony internetowej
    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'

    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text, 'html.parser')

    # pobranie współrzędnych z strony internetowej
    response_html_latitude = response_html.select('.latitude')[1].text  # . bo class
    response_html_latitude = float(response_html_latitude.replace(',', '.'))
    response_html_longitude = response_html.select('.longitude')[1].text  # . bo class
    response_html_longitude = float(response_html_longitude.replace(',', '.'))

    return [response_html_latitude, response_html_longitude]


# zwrócić mapę z pinezką odnoszącą się do użytkownika podanego z klawiatury
def get_ss_map_of() -> None:
    nick = input('Podaj nick użytkownika: ')
    sql_query_1 = f"SELECT * FROM public.watbook WHERE nick = '{nick}';"
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()

    if not query_result:
        print(f'Brak użytkownika o nicku {nick}')
        return

    cityuser_out = query_result[0]  # oddaje liste w nawiasach, więc trzeba jeszcze raz wywołać
    cityuser = cityuser_out[1]
    city = get_coordinate(cityuser)

    map = folium.Map(
        location=city,
        tiles="OpenStreetMap",
        zoom_start=15)
    for user in query_result:
        folium.Marker(
            location=city,
            popup=f'Tu rządzi {user[2]} z geoinformatyki 2023'
        ).add_to(map)

        map.save(f'Mapka{user[2]}.html')


# zwróci mapę z wszystkimi użytownikami z danej listy (znajomych)
def get_map_of() -> None:
    map = folium.Map(
        location=[52.3, 21.0],  # miejsce wysrodkowania mapy
        tiles="OpenStreetMap",
        zoom_start=7)
    sql_query_1 = f"SELECT * FROM public.watbook;"
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()

    for item in query_result:
        folium.Marker(
            location=get_coordinate(city=item[1]),
            popup=f'Użytkownik: {item[2]} \n'
                  f' Liczba postów: {item[4]}'
        ).add_to(map)

        map.save('Mapka.html')


def pogoda_z_(miasto: str):
    url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}"
    return requests.get(url).json()


def gui() -> None:
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
                show_users_from()
            case 2:
                print('Dodawanie użytkownika')
                add_user_to()
            case 3:
                print('Usuwanie użytkownika')
                remove_user_from()
            case 4:
                print('Edytowanie użytkownika')
                update_user()
            case 5:
                print('Tworzę mapę z lokalizacją użytkownika')
                get_ss_map_of()

            case 6:
                print('Tworzę mapę wszystkich użytkowników')
                get_map_of()


class User:
    def __init__(self, city, name, nick, posts):
        self.city = city
        self.name = name
        self.nick = nick
        self.posts = posts

    def pogoda_z_(self, miasto: str):
        URL = f'https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}'
        return requests.get(URL).json()


npc_1 = User(city='gdansk', name='Karol', nick='Lachon', posts=52532)
npc_2 = User(city='warszawa', name='Kacper', nick='szysza', posts=1231)

print(npc_1.city)
print(npc_2.city)

print(npc_1.pogoda_z_(npc_1.city))
print(npc_2.pogoda_z_(npc_2.city))



# def dodaj_użytkownika(user:str): ##Dodawanie z listy do tabeli
#     for nick in users_list:
#         if user == nick['nick']:
#             sql_query_1 = f"INSERT INTO public.watbook(city, name, nick, posts) VALUES ('{nick['city']}',  '{nick['name']}', '{nick['nick']}', '{nick['posts']}');"
#             cursor.execute(sql_query_1)
#             db_params.commit()
#
# dodaj_użytkownika(input('Podaj nick użytkownika do dodania z listy'))