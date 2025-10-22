from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from src.models import TipoDeGasto
from src.schemas import TipoDeGastoCreate, TipoDeGastoUpdate


class TipoDeGastoService:
    def __init__(self, db: Session):
        self.db = db

    def criar_tipo_gasto(self, tipo_gasto_data: TipoDeGastoCreate) -> TipoDeGasto:
        """Cria um novo tipo de gasto"""
        try:
            tipo_gasto = TipoDeGasto(**tipo_gasto_data.dict())
            self.db.add(tipo_gasto)
            self.db.commit()
            self.db.refresh(tipo_gasto)
            return tipo_gasto
        except IntegrityError as e:
            self.db.rollback()
            raise ValueError(f"Tipo de gasto com esta descrição já existe: {str(e)}")

    def obter_tipo_gasto_por_id(self, tipo_gasto_id: int) -> Optional[TipoDeGasto]:
        """Obtém um tipo de gasto por ID"""
        return self.db.query(TipoDeGasto).filter(TipoDeGasto.id == tipo_gasto_id).first()

    def obter_todos_tipos_gasto(self, skip: int = 0, limit: int = 100) -> List[TipoDeGasto]:
        """Obtém todos os tipos de gasto com paginação"""
        return self.db.query(TipoDeGasto).offset(skip).limit(limit).all()

    def atualizar_tipo_gasto(self, tipo_gasto_id: int, tipo_gasto_data: TipoDeGastoUpdate) -> Optional[TipoDeGasto]:
        """Atualiza um tipo de gasto existente"""
        tipo_gasto = self.obter_tipo_gasto_por_id(tipo_gasto_id)
        if not tipo_gasto:
            return None
        
        try:
            update_data = tipo_gasto_data.dict(exclude_unset=True)
            for field, value in update_data.items():
                setattr(tipo_gasto, field, value)
            
            self.db.commit()
            self.db.refresh(tipo_gasto)
            return tipo_gasto
        except IntegrityError as e:
            self.db.rollback()
            raise ValueError(f"Tipo de gasto com esta descrição já existe: {str(e)}")

    def deletar_tipo_gasto(self, tipo_gasto_id: int) -> bool:
        """Deleta um tipo de gasto"""
        tipo_gasto = self.obter_tipo_gasto_por_id(tipo_gasto_id)
        if not tipo_gasto:
            return False
        
        self.db.delete(tipo_gasto)
        self.db.commit()
        return True

    def obter_tipo_gasto_por_descricao(self, descricao: str) -> Optional[TipoDeGasto]:
        """Obtém um tipo de gasto por descrição"""
        return self.db.query(TipoDeGasto).filter(TipoDeGasto.descricao == descricao).first()
