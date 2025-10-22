from pydantic import BaseModel, Field
from typing import Optional, List
from .registro_schema import RegistroResponse


class TipoDeGastoBase(BaseModel):
    descricao: str = Field(..., min_length=1, max_length=50, description="Descrição do tipo de gasto")


class TipoDeGastoCreate(TipoDeGastoBase):
    pass


class TipoDeGastoUpdate(BaseModel):
    descricao: Optional[str] = Field(None, min_length=1, max_length=50, description="Descrição do tipo de gasto")


class TipoDeGastoResponse(TipoDeGastoBase):
    id: int
    registros: List[RegistroResponse] = []
    
    class Config:
        orm_mode = True
