import folium
import requests
import sqlalchemy.orm
import os
from dane import users_list
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
from dml import db_params


load_dotenv()
engine = sqlalchemy.create_engine(db_params)
connection = engine.connect()
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session
Base = sqlalchemy.orm.declarative_base()

def add_user(users_list:list) -> None:
    name = input('podaj imię')
    nick = input('podaj nick')
    posts = input('podaj liczbę postów')
    city = input('podaj miejscowość')
    users_list.append({"name": name, "nick": nick, "city": city, "posts": posts})

def remove_user_from(users_list: list) -> None:
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
            print('taki ćwok istnieje')
            user['name'] = input('podaj nowe imię: ')
            user['nick'] = input('Podaj nową ksywę: ')
            user['city'] = input('Podaj nową miejscowość: ')
            user['posts'] = int(input('podaj liczbę postów: '))

