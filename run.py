#!/usr/bin/env python3
"""
Script para executar a API KAIROS
"""

import uvicorn
import os
from dotenv import load_dotenv

def main():
    """Executa a API com configurações do ambiente"""
    # Carregar variáveis de ambiente
    load_dotenv()
    
    # Configurações padrão
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 8000))
    debug = os.getenv("API_DEBUG", "True").lower() == "true"
    
    print("🚀 Iniciando API KAIROS...")
    print(f"📍 Host: {host}")
    print(f"🔌 Porta: {port}")
    print(f"🐛 Debug: {debug}")
    print(f"📚 Documentação: http://{host}:{port}/docs")
    print("=" * 50)
    
    # Executar a API
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=debug,
        log_level="info" if debug else "warning"
    )

if __name__ == "__main__":
    main()
