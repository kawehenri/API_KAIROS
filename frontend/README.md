# 🎨 Frontend KAIROS

Interface web moderna e responsiva para o sistema de controle de gastos KAIROS.

## ✨ Funcionalidades

### 📊 Dashboard
- **Resumo Financeiro**: Total de gastos, tipos de gasto e registros
- **Últimos Gastos**: Lista dos 5 gastos mais recentes
- **Estatísticas Visuais**: Cards informativos com métricas importantes

### 🏷️ Gestão de Tipos de Gasto
- **Criar Tipos**: Adicionar novos tipos de gasto (Alimentação, Transporte, etc.)
- **Listar Tipos**: Visualizar todos os tipos cadastrados
- **Editar Tipos**: Modificar descrições existentes
- **Excluir Tipos**: Remover tipos não utilizados

### 💰 Gestão de Registros
- **Criar Registros**: Adicionar novos gastos com valor, tipo e observação
- **Listar Registros**: Visualizar todos os gastos registrados
- **Editar Registros**: Modificar valores e informações
- **Excluir Registros**: Remover registros incorretos

## 🎨 Design

### Características Visuais
- **Design Moderno**: Interface limpa e profissional
- **Responsivo**: Funciona em desktop, tablet e mobile
- **Tema Escuro**: Gradiente azul/roxo elegante
- **Ícones**: Font Awesome para melhor UX
- **Animações**: Transições suaves e feedback visual

### Componentes
- **Cards**: Informações organizadas em cards
- **Modais**: Formulários em pop-ups elegantes
- **Toast**: Notificações não intrusivas
- **Loading**: Indicadores de carregamento
- **Navegação**: Abas intuitivas

## 🛠️ Tecnologias

- **HTML5**: Estrutura semântica
- **CSS3**: Estilos modernos com Flexbox e Grid
- **JavaScript ES6+**: Lógica da aplicação
- **Fetch API**: Comunicação com a API
- **Font Awesome**: Ícones vetoriais

## 📱 Responsividade

### Breakpoints
- **Desktop**: > 768px - Layout em grid
- **Mobile**: ≤ 768px - Layout em coluna única

### Adaptações Mobile
- Navegação em coluna
- Modais em tela cheia
- Botões maiores para touch
- Formulários otimizados

## 🚀 Como Usar

### Acesso
1. Inicie a API: `python3 run.py`
2. Acesse: http://localhost:8000
3. O frontend será carregado automaticamente

### Navegação
- **Dashboard**: Visão geral dos gastos
- **Tipos de Gasto**: Gerenciar categorias
- **Registros**: Gerenciar gastos individuais

### Operações
1. **Criar**: Clique no botão "+" em cada seção
2. **Editar**: Clique no botão "Editar" de qualquer item
3. **Excluir**: Clique no botão "Excluir" (com confirmação)

## 🎯 Funcionalidades Especiais

### Validação
- **Campos Obrigatórios**: Validação no frontend
- **Valores Positivos**: Apenas valores válidos
- **Confirmações**: Diálogos para ações destrutivas

### Feedback
- **Loading**: Indicadores durante operações
- **Toast**: Notificações de sucesso/erro
- **Estados Vazios**: Mensagens quando não há dados

### UX/UI
- **Auto-focus**: Foco automático em campos
- **Enter para Submit**: Submissão com Enter
- **Escape para Fechar**: Fechar modais com Escape
- **Click Outside**: Fechar modais clicando fora

## 🔧 Estrutura de Arquivos

```
frontend/
├── index.html          # Página principal
├── css/
│   └── style.css       # Estilos da aplicação
├── js/
│   └── app.js          # Lógica JavaScript
└── README.md           # Esta documentação
```

## 🎨 Paleta de Cores

- **Primária**: #667eea (Azul)
- **Secundária**: #764ba2 (Roxo)
- **Sucesso**: #28a745 (Verde)
- **Erro**: #dc3545 (Vermelho)
- **Aviso**: #ffc107 (Amarelo)
- **Info**: #17a2b8 (Ciano)

## 📊 Componentes Principais

### Dashboard
- Cards de estatísticas
- Lista de últimos gastos
- Métricas em tempo real

### Formulários
- Modal de tipo de gasto
- Modal de registro
- Validação em tempo real

### Listas
- Tipos de gasto com ações
- Registros com detalhes
- Estados vazios informativos

## 🔄 Integração com API

### Endpoints Utilizados
- `GET /tipos-gasto/` - Listar tipos
- `POST /tipos-gasto/` - Criar tipo
- `PUT /tipos-gasto/{id}` - Atualizar tipo
- `DELETE /tipos-gasto/{id}` - Excluir tipo
- `GET /registros/` - Listar registros
- `POST /registros/` - Criar registro
- `PUT /registros/{id}` - Atualizar registro
- `DELETE /registros/{id}` - Excluir registro

### Tratamento de Erros
- Mensagens de erro amigáveis
- Fallbacks para falhas de rede
- Validação de dados

## 🚀 Melhorias Futuras

- [ ] Gráficos de gastos por categoria
- [ ] Filtros e busca avançada
- [ ] Exportação de dados
- [ ] Temas personalizáveis
- [ ] Modo offline
- [ ] PWA (Progressive Web App)
- [ ] Notificações push
- [ ] Relatórios em PDF
