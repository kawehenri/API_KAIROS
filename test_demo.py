#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de demonstração da API KAIROS
"""

import requests
import json
import time

BASE_URL = "http://localhost:8000"

def test_endpoint(method, endpoint, data=None, description=""):
    """Testa um endpoint da API"""
    url = f"{BASE_URL}{endpoint}"
    print(f"\n🔄 {description}")
    print(f"   {method} {endpoint}")
    
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)
        elif method == "PUT":
            response = requests.put(url, json=data)
        elif method == "DELETE":
            response = requests.delete(url)
        
        if response.status_code < 400:
            print(f"   ✅ Status: {response.status_code}")
            if response.content:
                result = response.json()
                print(f"   📄 Resposta: {json.dumps(result, indent=2, ensure_ascii=False)}")
        else:
            print(f"   ❌ Status: {response.status_code}")
            print(f"   📄 Erro: {response.text}")
            
    except Exception as e:
        print(f"   ❌ Erro: {str(e)}")

def main():
    """Executa demonstração completa da API"""
    print("🚀 DEMONSTRAÇÃO DA API KAIROS")
    print("=" * 50)
    
    # Aguardar API estar pronta
    print("⏳ Aguardando API estar pronta...")
    time.sleep(2)
    
    # Testar endpoints básicos
    test_endpoint("GET", "/", description="Informações da API")
    test_endpoint("GET", "/health", description="Health Check")
    
    # Testar tipos de gasto
    print("\n📋 TESTANDO TIPOS DE GASTO")
    print("-" * 30)
    
    test_endpoint("GET", "/tipos-gasto/", description="Listar tipos de gasto")
    
    test_endpoint("POST", "/tipos-gasto/", 
                 {"descricao": "Lazer"}, 
                 "Criar tipo de gasto 'Lazer'")
    
    test_endpoint("POST", "/tipos-gasto/", 
                 {"descricao": "Saúde"}, 
                 "Criar tipo de gasto 'Saúde'")
    
    test_endpoint("GET", "/tipos-gasto/", description="Listar tipos após criação")
    
    test_endpoint("GET", "/tipos-gasto/1", description="Obter tipo específico (ID 1)")
    
    test_endpoint("PUT", "/tipos-gasto/1", 
                 {"descricao": "Alimentação e Bebidas"}, 
                 "Atualizar tipo de gasto")
    
    # Testar registros
    print("\n💰 TESTANDO REGISTROS DE GASTO")
    print("-" * 30)
    
    test_endpoint("GET", "/registros/", description="Listar registros")
    
    test_endpoint("POST", "/registros/", 
                 {"vlr_gasto": 15.00, "observacao": "Cinema", "fk_tipo_gasto": 3}, 
                 "Criar registro de gasto")
    
    test_endpoint("POST", "/registros/", 
                 {"vlr_gasto": 80.00, "observacao": "Consulta médica", "fk_tipo_gasto": 4}, 
                 "Criar outro registro")
    
    test_endpoint("GET", "/registros/", description="Listar registros após criação")
    
    test_endpoint("GET", "/registros/1", description="Obter registro específico")
    
    test_endpoint("PUT", "/registros/1", 
                 {"vlr_gasto": 20.00}, 
                 "Atualizar valor do registro")
    
    test_endpoint("GET", "/registros/tipo-gasto/3", description="Registros por tipo de gasto")
    
    print("\n" + "=" * 50)
    print("🎉 DEMONSTRAÇÃO CONCLUÍDA!")
    print("\n📚 Acesse a documentação em: http://localhost:8000/docs")
    print("🔍 Health check em: http://localhost:8000/health")

if __name__ == "__main__":
    main()
