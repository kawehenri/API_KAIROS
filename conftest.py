"""
Configuração para testes da API KAIROS
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from main import app
from src.connection import Base, get_db
from src.models import Registro, TipoDeGasto

# Configurar banco de dados em memória para testes
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    """Override da dependência get_db para testes"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

@pytest.fixture(scope="function")
def db_session():
    """Fixture para sessão de banco de dados de teste"""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db_session):
    """Fixture para cliente de teste"""
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()

@pytest.fixture
def sample_tipo_gasto(db_session):
    """Fixture para criar um tipo de gasto de exemplo"""
    tipo_gasto = TipoDeGasto(descricao="Alimentação")
    db_session.add(tipo_gasto)
    db_session.commit()
    db_session.refresh(tipo_gasto)
    return tipo_gasto

@pytest.fixture
def sample_registro(db_session, sample_tipo_gasto):
    """Fixture para criar um registro de exemplo"""
    registro = Registro(
        vlr_gasto=25.50,
        observacao="Almoço no restaurante",
        fk_tipo_gasto=sample_tipo_gasto.id
    )
    db_session.add(registro)
    db_session.commit()
    db_session.refresh(registro)
    return registro
