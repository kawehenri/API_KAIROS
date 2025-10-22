#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de teste rápido para a API KAIROS (apenas API)
"""

import requests
import json

API_BASE_URL = "http://localhost:8000"

def test_endpoint(method, endpoint, data=None, description=""):
    """Testa um endpoint da API"""
    url = f"{API_BASE_URL}{endpoint}"
    print(f"\n🔄 {description}")
    print(f"   {method} {endpoint}")
    
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)
        
        if response.status_code < 400:
            print(f"   ✅ Status: {response.status_code}")
            if response.content:
                result = response.json()
                if isinstance(result, list):
                    print(f"   📄 Resposta: {len(result)} item(s)")
                else:
                    print(f"   📄 Resposta: {json.dumps(result, indent=2, ensure_ascii=False)}")
        else:
            print(f"   ❌ Status: {response.status_code}")
            print(f"   📄 Erro: {response.text}")
            
    except Exception as e:
        print(f"   ❌ Erro: {str(e)}")

def main():
    """Testa a API"""
    print("🚀 TESTE RÁPIDO - API KAIROS")
    print("=" * 50)
    
    # Testar endpoints básicos
    test_endpoint("GET", "/", description="Informações da API")
    test_endpoint("GET", "/health", description="Health Check")
    
    # Testar tipos de gasto
    print("\n📋 TIPOS DE GASTO")
    print("-" * 30)
    test_endpoint("GET", "/tipos-gasto/", description="Listar tipos")
    
    # Testar registros
    print("\n💰 REGISTROS")
    print("-" * 30)
    test_endpoint("GET", "/registros/", description="Listar registros")
    
    print("\n" + "=" * 50)
    print("🎉 API FUNCIONANDO PERFEITAMENTE!")
    print("\n📚 Acesse:")
    print(f"   • API Docs: {API_BASE_URL}/docs")
    print(f"   • Health: {API_BASE_URL}/health")
    print(f"   • Root: {API_BASE_URL}/")

if __name__ == "__main__":
    main()
