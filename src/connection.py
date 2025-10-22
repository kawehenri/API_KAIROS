from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db = os.getenv("DB_NAME")
port = os.getenv('DB_PORT')


DATABASE_URL = f'postgresql://{user}:{password}@{host}:{port}/{db}'

engine = create_engine(DATABASE_URL)

session = sessionmaker(autocommit= False, bind=engine)

Base = declarative_base()


def teste_conexao():
    try:
        with engine.connect() as connection:
            print ('conexao bem sucedida')
        
    except Exception as e:
        print(f'falha ao conectar com banco: {e}')

if __name__ == '__main__':
    teste_conexao()