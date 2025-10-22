from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class RegistroBase(BaseModel):
    vlr_gasto: float = Field(..., gt=0, description="Valor do gasto deve ser maior que zero")
    observacao: Optional[str] = Field(None, max_length=500, description="Observação sobre o gasto")
    fk_tipo_gasto: int = Field(..., description="ID do tipo de gasto")


class RegistroCreate(RegistroBase):
    pass


class RegistroUpdate(BaseModel):
    vlr_gasto: Optional[float] = Field(None, gt=0, description="Valor do gasto deve ser maior que zero")
    observacao: Optional[str] = Field(None, max_length=500, description="Observação sobre o gasto")
    fk_tipo_gasto: Optional[int] = Field(None, description="ID do tipo de gasto")


class RegistroResponse(RegistroBase):
    id: int
    dt_hr_gasto: datetime
    
    class Config:
        orm_mode = True
