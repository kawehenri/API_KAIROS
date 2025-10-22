from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class TipoDeGasto():
    __tablename__ = 'tipos_de_gasto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(50), nullable=False, unique=True)

    registros = relationship("Registro", back_populates="tipo_gasto", cascade="all, delete-orphan")