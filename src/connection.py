from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

# Configuração do banco de dados
DB_TYPE = os.getenv("DB_TYPE", "sqlite")  # sqlite ou postgresql

if DB_TYPE == "postgresql":
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    db = os.getenv("DB_NAME")
    port = os.getenv('DB_PORT')
    DATABASE_URL = f'postgresql://{user}:{password}@{host}:{port}/{db}'
else:
    # SQLite para desenvolvimento
    DATABASE_URL = "sqlite:///./kairos.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DB_TYPE == "sqlite" else {})

SessionLocal = sessionmaker(autocommit=False, bind=engine)

Base = declarative_base()


def get_db():
    """Dependency para obter sessão do banco de dados"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def teste_conexao():
    """Testa a conexão com o banco de dados"""
    try:
        with engine.connect() as connection:
            print('✅ Conexão com banco de dados bem sucedida')
            return True
    except Exception as e:
        print(f'❌ Falha ao conectar com banco: {e}')
        return False


if __name__ == '__main__':
    teste_conexao()