from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from src.models import Registro
from src.schemas import RegistroCreate, RegistroUpdate


class RegistroService:
    def __init__(self, db: Session):
        self.db = db

    def criar_registro(self, registro_data: RegistroCreate) -> Registro:
        """Cria um novo registro de gasto"""
        try:
            registro = Registro(**registro_data.dict())
            self.db.add(registro)
            self.db.commit()
            self.db.refresh(registro)
            return registro
        except IntegrityError as e:
            self.db.rollback()
            raise ValueError(f"Erro ao criar registro: {str(e)}")

    def obter_registro_por_id(self, registro_id: int) -> Optional[Registro]:
        """Obtém um registro por ID"""
        return self.db.query(Registro).filter(Registro.id == registro_id).first()

    def obter_todos_registros(self, skip: int = 0, limit: int = 100) -> List[Registro]:
        """Obtém todos os registros com paginação"""
        return self.db.query(Registro).offset(skip).limit(limit).all()

    def atualizar_registro(self, registro_id: int, registro_data: RegistroUpdate) -> Optional[Registro]:
        """Atualiza um registro existente"""
        registro = self.obter_registro_por_id(registro_id)
        if not registro:
            return None
        
        try:
            update_data = registro_data.dict(exclude_unset=True)
            for field, value in update_data.items():
                setattr(registro, field, value)
            
            self.db.commit()
            self.db.refresh(registro)
            return registro
        except IntegrityError as e:
            self.db.rollback()
            raise ValueError(f"Erro ao atualizar registro: {str(e)}")

    def deletar_registro(self, registro_id: int) -> bool:
        """Deleta um registro"""
        registro = self.obter_registro_por_id(registro_id)
        if not registro:
            return False
        
        self.db.delete(registro)
        self.db.commit()
        return True

    def obter_registros_por_tipo_gasto(self, tipo_gasto_id: int) -> List[Registro]:
        """Obtém todos os registros de um tipo de gasto específico"""
        return self.db.query(Registro).filter(Registro.fk_tipo_gasto == tipo_gasto_id).all()
