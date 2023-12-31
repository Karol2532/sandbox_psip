import sqlalchemy
import os
import sqlalchemy.orm
import random
from faker import Faker
from geoalchemy2 import Geometry
from dotenv import load_dotenv
from dml import User

load_dotenv()

db_params = sqlalchemy.URL.create(
    drivername='postgresql+psycopg2',
    username=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    database=os.getenv('POSTGRES_DB'),
    port=os.getenv('POSTGRES_PORT')
)

engine = sqlalchemy.create_engine(db_params)
connection = engine.connect()

Base = sqlalchemy.orm.declarative_base()


Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

#CREATE / insert
lista_userow: list =[]
fake = Faker()


for item in range(10_000):
    lista_userow.append(User(
        name=fake.name(),
        location=f'POINT({random.uniform(14,24)} {random.uniform(49,55)})'
    ))

session.add_all(lista_userow)
session.commit()

# Read / Select

users_from_db = session.query(User).all()
print(users_from_db)

#Update

users_from_db = session.query(User).all()
for user in users_from_db:
    if user.name == 'Brandon King':
        user.name = 'Karol Laska'
    print(user.name)


#Delete


session.flush()
connection.close()
engine.dispose()
