from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.connection import get_db
from src.services import RegistroService
from src.schemas import RegistroCreate, RegistroResponse, RegistroUpdate

router = APIRouter(prefix="/registros", tags=["registros"])


@router.post("/", response_model=RegistroResponse, status_code=status.HTTP_201_CREATED)
def criar_registro(registro_data: RegistroCreate, db: Session = Depends(get_db)):
    """Cria um novo registro de gasto"""
    try:
        service = RegistroService(db)
        return service.criar_registro(registro_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/", response_model=List[RegistroResponse])
def obter_registros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtém todos os registros com paginação"""
    service = RegistroService(db)
    return service.obter_todos_registros(skip=skip, limit=limit)


@router.get("/{registro_id}", response_model=RegistroResponse)
def obter_registro(registro_id: int, db: Session = Depends(get_db)):
    """Obtém um registro específico por ID"""
    service = RegistroService(db)
    registro = service.obter_registro_por_id(registro_id)
    if not registro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registro não encontrado"
        )
    return registro


@router.put("/{registro_id}", response_model=RegistroResponse)
def atualizar_registro(
    registro_id: int,
    registro_data: RegistroUpdate,
    db: Session = Depends(get_db)
):
    """Atualiza um registro existente"""
    try:
        service = RegistroService(db)
        registro = service.atualizar_registro(registro_id, registro_data)
        if not registro:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Registro não encontrado"
            )
        return registro
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{registro_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_registro(registro_id: int, db: Session = Depends(get_db)):
    """Deleta um registro"""
    service = RegistroService(db)
    if not service.deletar_registro(registro_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registro não encontrado"
        )


@router.get("/tipo-gasto/{tipo_gasto_id}", response_model=List[RegistroResponse])
def obter_registros_por_tipo_gasto(tipo_gasto_id: int, db: Session = Depends(get_db)):
    """Obtém todos os registros de um tipo de gasto específico"""
    service = RegistroService(db)
    return service.obter_registros_por_tipo_gasto(tipo_gasto_id)
