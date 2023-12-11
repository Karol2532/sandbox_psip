import sqlalchemy

db_params = sqlalchemy.URL.create(
    drivername='postgresql+psycopg2',
    username='postgres',
    password='123',
    host='localhost',
    database='postgres',
    port=5432
)
engine = sqlalchemy.create_engine(db_params)
connection = engine.connect()