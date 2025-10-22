# 🚀 Quick Start - API KAIROS

## ⚡ Execução Rápida

### 1. Configuração Inicial
```bash
# Copiar arquivo de configuração
cp env.example .env

# Editar variáveis de ambiente (importante!)
nano .env
```

### 2. Instalação e Setup
```bash
# Instalar dependências
pip install -r requirements.txt

# Executar setup automático
python setup.py
```

### 3. Executar a API
```bash
# Opção 1: Script personalizado
python run.py

# Opção 2: Uvicorn direto
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Acessar a API
- **API**: http://localhost:8000
- **Documentação**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 🔧 Configuração do Banco

### PostgreSQL
```sql
-- Criar banco de dados
CREATE DATABASE kairos_db;

-- Criar usuário (opcional)
CREATE USER kairos_user WITH PASSWORD 'sua_senha';
GRANT ALL PRIVILEGES ON DATABASE kairos_db TO kairos_user;
```

### Variáveis de Ambiente (.env)
```env
DB_HOST=localhost
DB_USER=kairos_user
DB_PASSWORD=sua_senha
DB_NAME=kairos_db
DB_PORT=5432
```

## 📋 Endpoints Principais

### Tipos de Gasto
```bash
# Criar tipo
curl -X POST "http://localhost:8000/tipos-gasto/" \
     -H "Content-Type: application/json" \
     -d '{"descricao": "Alimentação"}'

# Listar tipos
curl "http://localhost:8000/tipos-gasto/"
```

### Registros
```bash
# Criar registro
curl -X POST "http://localhost:8000/registros/" \
     -H "Content-Type: application/json" \
     -d '{
       "vlr_gasto": 25.50,
       "observacao": "Almoço",
       "fk_tipo_gasto": 1
     }'

# Listar registros
curl "http://localhost:8000/registros/"
```

## 🧪 Testes
```bash
# Executar testes
pytest test_api.py -v

# Executar com coverage
pytest test_api.py --cov=src --cov-report=html
```

## 🐛 Troubleshooting

### Erro de Conexão com Banco
1. Verifique se o PostgreSQL está rodando
2. Confirme as credenciais no arquivo `.env`
3. Teste a conexão: `python src/connection.py`

### Erro de Migração
```bash
# Recriar migração
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### Erro de Dependências
```bash
# Reinstalar dependências
pip install -r requirements.txt --force-reinstall
```

## 📚 Próximos Passos

1. **Autenticação**: Implementar JWT
2. **Validações**: Adicionar mais validações de negócio
3. **Relatórios**: Endpoints para relatórios de gastos
4. **Cache**: Implementar Redis para cache
5. **Logs**: Sistema de logging estruturado

## 🆘 Suporte

- **Documentação**: http://localhost:8000/docs
- **Issues**: Abra uma issue no repositório
- **Logs**: Verifique os logs da aplicação
