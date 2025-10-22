# API KAIROS

API para controle de gastos pessoais desenvolvida com FastAPI, SQLAlchemy e PostgreSQL.

## 🚀 Funcionalidades

### Backend (API)
- **Gestão de Tipos de Gasto**: Criar, listar, atualizar e deletar tipos de gasto
- **Gestão de Registros**: Criar, listar, atualizar e deletar registros de gastos
- **Relacionamentos**: Cada registro está associado a um tipo de gasto
- **Validação de Dados**: Validação automática com Pydantic
- **Documentação Automática**: Swagger UI disponível em `/docs`

### Frontend (Interface Web)
- **Dashboard Interativo**: Resumo financeiro e últimas transações
- **Interface Moderna**: Design responsivo e intuitivo
- **Gestão Visual**: CRUD completo com interface amigável
- **Notificações**: Feedback visual para todas as operações
- **Responsivo**: Funciona em desktop, tablet e mobile

## 📋 Pré-requisitos

- Python 3.8+
- PostgreSQL
- pip ou pipenv

## 🛠️ Instalação

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd API_KAIROS
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Configure as variáveis de ambiente**
```bash
cp env.example .env
# Edite o arquivo .env com suas configurações
```

4. **Configure o banco de dados**
```bash
# Crie o banco de dados PostgreSQL
createdb kairos_db

# Execute as migrações
alembic upgrade head
```

## 🚀 Executando a API

```bash
# Desenvolvimento
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Produção
uvicorn main:app --host 0.0.0.0 --port 8000
```

A aplicação estará disponível em: `http://localhost:8000` (Frontend) ou `http://localhost:8000/docs` (API Docs)

## 📚 Documentação da API

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🗂️ Estrutura do Projeto

```
API_KAIROS/
├── src/
│   ├── controllers/          # Rotas da API
│   ├── models/              # Modelos do banco de dados
│   ├── schemas/             # Schemas Pydantic
│   ├── services/            # Lógica de negócio
│   └── connection.py        # Configuração do banco
├── alembic/                 # Migrações do banco
├── main.py                  # Aplicação principal
├── requirements.txt         # Dependências
└── README.md               # Este arquivo
```

## 🔧 Endpoints Principais

### Tipos de Gasto
- `GET /tipos-gasto/` - Listar todos os tipos
- `POST /tipos-gasto/` - Criar novo tipo
- `GET /tipos-gasto/{id}` - Obter tipo específico
- `PUT /tipos-gasto/{id}` - Atualizar tipo
- `DELETE /tipos-gasto/{id}` - Deletar tipo

### Registros
- `GET /registros/` - Listar todos os registros
- `POST /registros/` - Criar novo registro
- `GET /registros/{id}` - Obter registro específico
- `PUT /registros/{id}` - Atualizar registro
- `DELETE /registros/{id}` - Deletar registro
- `GET /registros/tipo-gasto/{id}` - Registros por tipo

## 🗄️ Migrações

```bash
# Criar nova migração
alembic revision --autogenerate -m "Descrição da migração"

# Aplicar migrações
alembic upgrade head

# Reverter migração
alembic downgrade -1
```

## 🧪 Testes

```bash
# Instalar dependências de teste
pip install pytest pytest-asyncio httpx

# Executar testes
pytest
```

## 🔒 Variáveis de Ambiente

```env
# Banco de dados
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=kairos_db
DB_PORT=5432

# API
API_HOST=0.0.0.0
API_PORT=8000
API_DEBUG=True
```

## 📝 Exemplo de Uso

### Criar um tipo de gasto
```bash
curl -X POST "http://localhost:8000/tipos-gasto/" \
     -H "Content-Type: application/json" \
     -d '{"descricao": "Alimentação"}'
```

### Criar um registro de gasto
```bash
curl -X POST "http://localhost:8000/registros/" \
     -H "Content-Type: application/json" \
     -d '{
       "vlr_gasto": 25.50,
       "observacao": "Almoço no restaurante",
       "fk_tipo_gasto": 1
     }'
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
