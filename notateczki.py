import sqlalchemy
import os
import sqlalchemy.orm
import random
from faker import Faker
from geoalchemy2 import Geometry
from dotenv import load_dotenv

#import sqlalchemy
# import psycopg2
# from dane import users_list
# # Dodawanie z listy uzytkownikow do bazy danych
# db_params = psycopg2.connect(
#     database='postgres',
#     user='postgres',
#     password='123',
#     host='localhost',
#     port=5433
# )
#
# cursor = db_params.cursor()

# engine = sqlalchemy.create_engine(db_params)
# connection = engine.connect()

#sql_query_1 = sqlalchemy.text("INSERT INTO public.my_table(name) VALUES ('koc');")
#sql_query_1 = sqlalchemy.text("select * from public.my_table;")

#user = input('Podaj nazwę użytkownika do usunięcia')
#sql_query_1 = sqlalchemy.text(f"DELETE FROM public.my_table WHERE name ='{user}';")

#kogo_zamienic = input('Podaj nazwę użytkownika do zamiany')
#na_kogo = input('Podaj na kogo zamienić')
#sql_query_1 = sqlalchemy.text(f"UPDATE public.my_table SET name='{na_kogo}' WHERE name='{kogo_zamienic}';")

# def dodaj_użytkownika(user:str):
#     for nick in users_list:
#         if user == nick['nick']:
#             sql_query_1 = f"INSERT INTO public.watbook(city, name, nick, posts) VALUES ('{nick['city']}',  '{nick['name']}', '{nick['nick']}', '{nick['posts']}');"
#             cursor.execute(sql_query_1)
#             db_params.commit()
#
# dodaj_użytkownika(input('Podaj nick użytkownika do dodania z listy'))

# def usuń_użytkownika(user:str):
#     sql_query_1 = sqlalchemy.text(f"DELETE FROM public.my_table WHERE name ='{user}';")
#     connection.execute(sql_query_1)
#     connection.commit()
#
#
# def aktualizuj_użytkownika(user_1:str, user_2:str):
#     sql_query_1 = sqlalchemy.text(f"UPDATE public.my_table SET name='{user_2}' WHERE name='{user_1}';")
#     connection.execute(sql_query_1)
#     connection.commit()
#
# aktualizuj_użytkownika(
#     user_1=input('Podaj nazwę użytkownika do zamiany'),
#     user_2=input('Podaj na kogo zamienić')




#connection.execute(sql_query_1)
#connection.commit()



##STARE
#
#
# load_dotenv()
#
#
# db_params = sqlalchemy.URL.create(
#     drivername='postgresql+psycopg2',
#     username=os.getenv('POSTGRES_USER'),
#     password=os.getenv('POSTGRES_PASSWORD'),
#     host=os.getenv('POSTGRES_HOST'),
#     database=os.getenv('POSTGRES_DB'),
#     port=os.getenv('POSTGRES_PORT')
# )
#
# engine = sqlalchemy.create_engine(db_params)
# connection = engine.connect()
#
#
# Base = sqlalchemy.orm.declarative_base()
#
#
# class User(Base):
#     __tablename__ = 'mytable'
#
#     id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True)
#     name = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
#     location = sqlalchemy.Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=True)
#
# Base.metadata.create_all(engine)
#
#
#
#
# Session = sqlalchemy.orm.sessionmaker(bind=engine)
# session = Session()
#
# ##CREATE / insert
# # lista_userow: list =[]
# # fake = Faker()
# #
# #
# # for item in range(10_000):
# #     lista_userow.append(User(
# #         name=fake.name(),
# #         location=f'POINT({random.uniform(14,24)} {random.uniform(49,55)})'
# #     ))
# #
# # session.add_all(lista_userow)
# # session.commit()
#
# ## Read / Select
#
# # users_from_db = session.query(User).all()
# # print(users_from_db)
#
# ##Update
#
# # users_from_db = session.query(User).all()
# # for user in users_from_db:
# #     if user.name == 'Brandon King':
# #         user.name = 'Karol Laska'
# #     print(user.name)
#
#
# ##Delete
#
#
#
#
#
# session.flush()
# connection.close()
# engine.dispose()
#
# ###sss

# TODO dodac tabele do bazy danych reprezentujaca uzytkownika
# TODO wlaczyc do kodu obsluge bazy danych
# TODO napisac klase uzytkownika o strukturze zgodnej z user_list (sama definicja)
# TODO sprawko z ww do 20.12 (sroda)
# ma zawierac: tytulowa
# spis
# opis kodu realiujacego zadanie rysowanie mapy uwzgledniajacy poszczegolne fiunkcje oraz ich skladnie
# zredaliwowany kod na Git
# podsumowanie i wsnioski koncowe, ss