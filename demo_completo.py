#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de demonstração completa da aplicação KAIROS
Inclui teste da API e informações sobre o frontend
"""

import requests
import json
import time
import webbrowser
from pathlib import Path

API_BASE_URL = "http://localhost:8000"

def print_header(title):
    """Imprime um cabeçalho formatado"""
    print("\n" + "=" * 60)
    print(f"🎯 {title}")
    print("=" * 60)

def print_section(title):
    """Imprime uma seção formatada"""
    print(f"\n📋 {title}")
    print("-" * 40)

def test_api_endpoint(method, endpoint, data=None, description=""):
    """Testa um endpoint da API"""
    url = f"{API_BASE_URL}{endpoint}"
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
                if isinstance(result, list):
                    print(f"   📄 Resposta: {len(result)} item(s) encontrado(s)")
                else:
                    print(f"   📄 Resposta: {json.dumps(result, indent=2, ensure_ascii=False)}")
        else:
            print(f"   ❌ Status: {response.status_code}")
            print(f"   📄 Erro: {response.text}")
            
    except Exception as e:
        print(f"   ❌ Erro: {str(e)}")

def check_api_status():
    """Verifica se a API está rodando"""
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API Status: {data['status']}")
            print(f"✅ Database: {data['database']}")
            return True
        else:
            print(f"❌ API retornou status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erro ao conectar com a API: {str(e)}")
        return False

def demo_api():
    """Demonstração da API"""
    print_section("TESTANDO ENDPOINTS DA API")
    
    # Testar endpoints básicos
    test_api_endpoint("GET", "/", description="Informações da API")
    test_api_endpoint("GET", "/health", description="Health Check")
    
    # Testar tipos de gasto
    print_section("TIPOS DE GASTO")
    test_api_endpoint("GET", "/tipos-gasto/", description="Listar tipos de gasto")
    
    test_api_endpoint("POST", "/tipos-gasto/", 
                     {"descricao": "Demonstração"}, 
                     "Criar tipo de gasto 'Demonstração'")
    
    test_api_endpoint("GET", "/tipos-gasto/", description="Listar tipos após criação")
    
    # Testar registros
    print_section("REGISTROS DE GASTO")
    test_api_endpoint("GET", "/registros/", description="Listar registros")
    
    test_api_endpoint("POST", "/registros/", 
                     {"vlr_gasto": 50.00, "observacao": "Gasto de demonstração", "fk_tipo_gasto": 1}, 
                     "Criar registro de gasto")
    
    test_api_endpoint("GET", "/registros/", description="Listar registros após criação")

def show_frontend_info():
    """Mostra informações sobre o frontend"""
    print_section("INFORMAÇÕES DO FRONTEND")
    
    print("🎨 Interface Web Moderna:")
    print("   • Dashboard interativo com resumo financeiro")
    print("   • Gestão visual de tipos de gasto")
    print("   • Gestão visual de registros")
    print("   • Design responsivo (desktop/mobile)")
    print("   • Notificações em tempo real")
    print("   • Modais elegantes para formulários")
    
    print("\n📱 Funcionalidades do Frontend:")
    print("   • Criar, editar e excluir tipos de gasto")
    print("   • Criar, editar e excluir registros")
    print("   • Visualizar estatísticas no dashboard")
    print("   • Interface intuitiva e moderna")
    print("   • Feedback visual para todas as operações")
    
    print("\n🌐 Acesso:")
    print(f"   • Frontend: {API_BASE_URL}")
    print(f"   • API Docs: {API_BASE_URL}/docs")
    print(f"   • Health Check: {API_BASE_URL}/health")

def open_browser():
    """Abre o navegador com o frontend"""
    try:
        print(f"\n🌐 Abrindo frontend no navegador: {API_BASE_URL}")
        webbrowser.open(API_BASE_URL)
        print("✅ Navegador aberto com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao abrir navegador: {str(e)}")
        print(f"   Acesse manualmente: {API_BASE_URL}")

def show_project_structure():
    """Mostra a estrutura do projeto"""
    print_section("ESTRUTURA DO PROJETO")
    
    project_root = Path(".")
    structure = {
        "📁 API_KAIROS/": {
            "📄 main.py": "Aplicação principal FastAPI",
            "📄 run.py": "Script para executar a API",
            "📄 requirements.txt": "Dependências Python",
            "📁 src/": {
                "📁 models/": "Modelos do banco de dados",
                "📁 schemas/": "Schemas Pydantic",
                "📁 services/": "Lógica de negócio",
                "📁 controllers/": "Rotas da API",
                "📄 connection.py": "Conexão com banco"
            },
            "📁 frontend/": {
                "📄 index.html": "Página principal",
                "📁 css/": "Estilos da aplicação",
                "📁 js/": "Lógica JavaScript"
            },
            "📁 alembic/": "Migrações do banco"
        }
    }
    
    def print_structure(items, indent=0):
        for key, value in items.items():
            print("  " * indent + key)
            if isinstance(value, dict):
                print_structure(value, indent + 1)
            else:
                print("  " * (indent + 1) + f"→ {value}")
    
    print_structure(structure)

def main():
    """Função principal da demonstração"""
    print_header("DEMONSTRAÇÃO COMPLETA - KAIROS")
    print("Sistema completo de controle de gastos pessoais")
    print("Backend: FastAPI + SQLAlchemy + SQLite")
    print("Frontend: HTML5 + CSS3 + JavaScript")
    
    # Verificar status da API
    print_section("VERIFICANDO STATUS DA API")
    if not check_api_status():
        print("\n❌ A API não está rodando!")
        print("   Execute: python3 run.py")
        return
    
    # Mostrar estrutura do projeto
    show_project_structure()
    
    # Demonstrar API
    demo_api()
    
    # Mostrar informações do frontend
    show_frontend_info()
    
    # Perguntar se quer abrir o navegador
    print_section("ACESSO À APLICAÇÃO")
    try:
        resposta = input("Deseja abrir o frontend no navegador? (s/n): ").lower().strip()
        if resposta in ['s', 'sim', 'y', 'yes']:
            open_browser()
    except KeyboardInterrupt:
        print("\n\n👋 Demonstração interrompida pelo usuário")
        return
    
    print_header("DEMONSTRAÇÃO CONCLUÍDA!")
    print("🎉 A aplicação KAIROS está funcionando perfeitamente!")
    print("\n📚 Recursos disponíveis:")
    print(f"   • Frontend: {API_BASE_URL}")
    print(f"   • API Docs: {API_BASE_URL}/docs")
    print(f"   • Health Check: {API_BASE_URL}/health")
    print("\n🚀 Próximos passos:")
    print("   • Explore o frontend interativo")
    print("   • Teste todas as funcionalidades")
    print("   • Consulte a documentação da API")
    print("   • Personalize conforme suas necessidades")

if __name__ == "__main__":
    main()
