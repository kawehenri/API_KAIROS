"""
Testes básicos para a API KAIROS
"""

import pytest
from fastapi.testclient import TestClient


class TestTipoDeGasto:
    """Testes para endpoints de tipos de gasto"""
    
    def test_criar_tipo_gasto(self, client: TestClient):
        """Testa criação de tipo de gasto"""
        response = client.post(
            "/tipos-gasto/",
            json={"descricao": "Alimentação"}
        )
        assert response.status_code == 201
        data = response.json()
        assert data["descricao"] == "Alimentação"
        assert "id" in data
    
    def test_listar_tipos_gasto(self, client: TestClient, sample_tipo_gasto):
        """Testa listagem de tipos de gasto"""
        response = client.get("/tipos-gasto/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["descricao"] == "Alimentação"
    
    def test_obter_tipo_gasto_por_id(self, client: TestClient, sample_tipo_gasto):
        """Testa obtenção de tipo de gasto por ID"""
        response = client.get(f"/tipos-gasto/{sample_tipo_gasto.id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == sample_tipo_gasto.id
        assert data["descricao"] == "Alimentação"
    
    def test_atualizar_tipo_gasto(self, client: TestClient, sample_tipo_gasto):
        """Testa atualização de tipo de gasto"""
        response = client.put(
            f"/tipos-gasto/{sample_tipo_gasto.id}",
            json={"descricao": "Alimentação e Bebidas"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["descricao"] == "Alimentação e Bebidas"
    
    def test_deletar_tipo_gasto(self, client: TestClient, sample_tipo_gasto):
        """Testa deleção de tipo de gasto"""
        response = client.delete(f"/tipos-gasto/{sample_tipo_gasto.id}")
        assert response.status_code == 204
        
        # Verificar se foi deletado
        response = client.get(f"/tipos-gasto/{sample_tipo_gasto.id}")
        assert response.status_code == 404


class TestRegistro:
    """Testes para endpoints de registros"""
    
    def test_criar_registro(self, client: TestClient, sample_tipo_gasto):
        """Testa criação de registro"""
        response = client.post(
            "/registros/",
            json={
                "vlr_gasto": 25.50,
                "observacao": "Almoço no restaurante",
                "fk_tipo_gasto": sample_tipo_gasto.id
            }
        )
        assert response.status_code == 201
        data = response.json()
        assert data["vlr_gasto"] == 25.50
        assert data["observacao"] == "Almoço no restaurante"
        assert data["fk_tipo_gasto"] == sample_tipo_gasto.id
        assert "id" in data
    
    def test_listar_registros(self, client: TestClient, sample_registro):
        """Testa listagem de registros"""
        response = client.get("/registros/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["vlr_gasto"] == 25.50
    
    def test_obter_registro_por_id(self, client: TestClient, sample_registro):
        """Testa obtenção de registro por ID"""
        response = client.get(f"/registros/{sample_registro.id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == sample_registro.id
        assert data["vlr_gasto"] == 25.50
    
    def test_atualizar_registro(self, client: TestClient, sample_registro):
        """Testa atualização de registro"""
        response = client.put(
            f"/registros/{sample_registro.id}",
            json={"vlr_gasto": 30.00}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["vlr_gasto"] == 30.00
    
    def test_deletar_registro(self, client: TestClient, sample_registro):
        """Testa deleção de registro"""
        response = client.delete(f"/registros/{sample_registro.id}")
        assert response.status_code == 204
        
        # Verificar se foi deletado
        response = client.get(f"/registros/{sample_registro.id}")
        assert response.status_code == 404


class TestEndpointsGerais:
    """Testes para endpoints gerais"""
    
    def test_root_endpoint(self, client: TestClient):
        """Testa endpoint raiz"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data
    
    def test_health_check(self, client: TestClient):
        """Testa endpoint de health check"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
