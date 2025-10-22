#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de configuração inicial para a API KAIROS
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Executa um comando e mostra o resultado"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} concluído com sucesso!")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao {description.lower()}:")
        print(f"   {e.stderr}")
        return False

def check_python_version():
    """Verifica se a versão do Python é compatível"""
    print("🐍 Verificando versão do Python...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ é necessário!")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detectado")
    return True

def check_env_file():
    """Verifica se o arquivo .env existe"""
    print("\n📄 Verificando arquivo de configuração...")
    env_file = Path(".env")
    if not env_file.exists():
        print("⚠️  Arquivo .env não encontrado!")
        print("   Copiando env.example para .env...")
        try:
            with open("env.example", "r") as src, open(".env", "w") as dst:
                dst.write(src.read())
            print("✅ Arquivo .env criado! Configure as variáveis de ambiente.")
        except FileNotFoundError:
            print("❌ Arquivo env.example não encontrado!")
            return False
    else:
        print("✅ Arquivo .env encontrado")
    return True

def install_dependencies():
    """Instala as dependências do projeto"""
    return run_command("pip install -r requirements.txt", "Instalando dependências")

def create_migration():
    """Cria a migração inicial"""
    return run_command("alembic revision --autogenerate -m 'Initial migration'", "Criando migração inicial")

def apply_migrations():
    """Aplica as migrações"""
    return run_command("alembic upgrade head", "Aplicando migrações")

def main():
    """Função principal do script de setup"""
    print("🚀 Configurando API KAIROS...")
    print("=" * 50)
    
    # Verificações iniciais
    if not check_python_version():
        sys.exit(1)
    
    if not check_env_file():
        sys.exit(1)
    
    # Instalação e configuração
    steps = [
        (install_dependencies, "Instalação de dependências"),
        (create_migration, "Criação de migração"),
        (apply_migrations, "Aplicação de migrações")
    ]
    
    for step_func, description in steps:
        if not step_func():
            print(f"\n❌ Falha na {description.lower()}")
            print("   Verifique os erros acima e tente novamente.")
            sys.exit(1)
    
    print("\n" + "=" * 50)
    print("🎉 Configuração concluída com sucesso!")
    print("\n📋 Próximos passos:")
    print("1. Configure as variáveis de ambiente no arquivo .env")
    print("2. Certifique-se de que o PostgreSQL está rodando")
    print("3. Execute: uvicorn main:app --reload")
    print("4. Acesse: http://localhost:8000/docs")
    print("\n📚 Documentação disponível em: http://localhost:8000/docs")

if __name__ == "__main__":
    main()
