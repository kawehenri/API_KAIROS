from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.connection import get_db
from src.services import TipoDeGastoService
from src.schemas import TipoDeGastoCreate, TipoDeGastoResponse, TipoDeGastoUpdate

router = APIRouter(prefix="/tipos-gasto", tags=["tipos-gasto"])


@router.post("/", response_model=TipoDeGastoResponse, status_code=status.HTTP_201_CREATED)
def criar_tipo_gasto(tipo_gasto_data: TipoDeGastoCreate, db: Session = Depends(get_db)):
    """Cria um novo tipo de gasto"""
    try:
        service = TipoDeGastoService(db)
        return service.criar_tipo_gasto(tipo_gasto_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/", response_model=List[TipoDeGastoResponse])
def obter_tipos_gasto(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtém todos os tipos de gasto com paginação"""
    service = TipoDeGastoService(db)
    return service.obter_todos_tipos_gasto(skip=skip, limit=limit)


@router.get("/{tipo_gasto_id}", response_model=TipoDeGastoResponse)
def obter_tipo_gasto(tipo_gasto_id: int, db: Session = Depends(get_db)):
    """Obtém um tipo de gasto específico por ID"""
    service = TipoDeGastoService(db)
    tipo_gasto = service.obter_tipo_gasto_por_id(tipo_gasto_id)
    if not tipo_gasto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tipo de gasto não encontrado"
        )
    return tipo_gasto


@router.put("/{tipo_gasto_id}", response_model=TipoDeGastoResponse)
def atualizar_tipo_gasto(
    tipo_gasto_id: int,
    tipo_gasto_data: TipoDeGastoUpdate,
    db: Session = Depends(get_db)
):
    """Atualiza um tipo de gasto existente"""
    try:
        service = TipoDeGastoService(db)
        tipo_gasto = service.atualizar_tipo_gasto(tipo_gasto_id, tipo_gasto_data)
        if not tipo_gasto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tipo de gasto não encontrado"
            )
        return tipo_gasto
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{tipo_gasto_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tipo_gasto(tipo_gasto_id: int, db: Session = Depends(get_db)):
    """Deleta um tipo de gasto"""
    service = TipoDeGastoService(db)
    if not service.deletar_tipo_gasto(tipo_gasto_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tipo de gasto não encontrado"
        )
