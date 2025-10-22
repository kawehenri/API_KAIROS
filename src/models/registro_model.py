from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from src.connection import Base

class Registro(Base):
    __tablename__ = 'registros'

    id = Column(Integer, primary_key=True, autoincrement=True)
    dt_hr_gasto = Column(DateTime, default=datetime.utcnow)
    vlr_gasto = Column(Float, nullable=False)
    observacao = Column(Text)

    fk_tipo_gasto = Column(Integer, ForeignKey('tipos_de_gasto.id'))

    tipo_gasto = relationship("TipoDeGasto", back_populates="registros")