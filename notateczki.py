import sqlalchemy

db_params = sqlalchemy.URL.create(
    drivername='postgresql+psycopg2',
    username='postgres',
    password='123',
    host='localhost',
    database='postgres',
    port=5433
)



engine = sqlalchemy.create_engine(db_params)
connection = engine.connect()

#sql_query_1 = sqlalchemy.text("INSERT INTO public.my_table(name) VALUES ('koc');")
#sql_query_1 = sqlalchemy.text("select * from public.my_table;")

#user = input('Podaj nazwę użytkownika do usunięcia')
#sql_query_1 = sqlalchemy.text(f"DELETE FROM public.my_table WHERE name ='{user}';")

#kogo_zamienic = input('Podaj nazwę użytkownika do zamiany')
#na_kogo = input('Podaj na kogo zamienić')
#sql_query_1 = sqlalchemy.text(f"UPDATE public.my_table SET name='{na_kogo}' WHERE name='{kogo_zamienic}';")
user = 'laska'
def dodaj_użytkownika(user:str):
    sql_query_1 = sqlalchemy.text("INSERT INTO public.my_table(name) VALUES ('{user}');")
    connection.execute(sql_query_1)
    connection.commit()


def usuń_użytkownika(user:str):
    sql_query_1 = sqlalchemy.text(f"DELETE FROM public.my_table WHERE name ='{user}';")
    connection.execute(sql_query_1)
    connection.commit()


def aktualizuj_użytkownika(user_1:str, user_2:str):
    sql_query_1 = sqlalchemy.text(f"UPDATE public.my_table SET name='{user_2}' WHERE name='{user_1}';")
    connection.execute(sql_query_1)
    connection.commit()

aktualizuj_użytkownika(
    user_1=input('Podaj nazwę użytkownika do zamiany'),
    user_2=input('Podaj na kogo zamienić')
)



#connection.execute(sql_query_1)
#connection.commit()