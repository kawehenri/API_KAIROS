from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
from src.connection import teste_conexao, Base, engine
from src.controllers import registro_router, tipo_de_gasto_router
import os

# Criar tabelas no banco de dados
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Iniciando API KAIROS...")
    try:
        # Testar conexão com o banco
        teste_conexao()
        
        # Criar tabelas se não existirem
        Base.metadata.create_all(bind=engine)
        print("Tabelas criadas/verificadas com sucesso!")
        
    except Exception as e:
        print(f"Erro ao inicializar: {e}")
        raise
    
    yield
    
    # Shutdown
    print("Finalizando API KAIROS...")

# Criar aplicação FastAPI
app = FastAPI(
    title="API KAIROS",
    description="API para controle de gastos pessoais",
    version="1.0.0",
    lifespan=lifespan
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas
app.include_router(registro_router)
app.include_router(tipo_de_gasto_router)

# Servir arquivos estáticos do frontend
frontend_path = os.path.join(os.path.dirname(__file__), "frontend")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")


@app.get("/")
async def root():
    """Endpoint raiz da API - serve o frontend"""
    frontend_file = os.path.join(frontend_path, "index.html")
    if os.path.exists(frontend_file):
        return FileResponse(frontend_file)
    else:
        return {
            "message": "Bem-vindo à API KAIROS",
            "version": "1.0.0",
            "description": "API para controle de gastos pessoais",
            "endpoints": {
                "docs": "/docs",
                "health": "/health",
                "tipos_gasto": "/tipos-gasto/",
                "registros": "/registros/"
            }
        }


@app.get("/health")
async def health_check():
    """Endpoint para verificar saúde da API"""
    try:
        teste_conexao()
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Database connection failed: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
