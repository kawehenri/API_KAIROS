// Configuração da API
const API_BASE_URL = 'http://localhost:8000';

// Estado global da aplicação
let tiposGasto = [];
let registros = [];

// Inicialização da aplicação
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

async function initializeApp() {
    showLoading();
    
    try {
        // Carregar dados iniciais
        await Promise.all([
            loadTiposGasto(),
            loadRegistros()
        ]);
        
        // Configurar navegação
        setupNavigation();
        
        // Configurar formulários
        setupForms();
        
        // Atualizar dashboard
        updateDashboard();
        
        hideLoading();
        showToast('Aplicação carregada com sucesso!', 'success');
        
    } catch (error) {
        hideLoading();
        showToast('Erro ao carregar dados: ' + error.message, 'error');
        console.error('Erro na inicialização:', error);
    }
}

// Navegação entre abas
function setupNavigation() {
    const tabs = document.querySelectorAll('.nav-tab');
    const contents = document.querySelectorAll('.tab-content');
    
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const targetTab = tab.getAttribute('data-tab');
            
            // Remover classe active de todas as abas
            tabs.forEach(t => t.classList.remove('active'));
            contents.forEach(c => c.classList.remove('active'));
            
            // Adicionar classe active na aba clicada
            tab.classList.add('active');
            document.getElementById(targetTab).classList.add('active');
        });
    });
}

// Configurar formulários
function setupForms() {
    // Formulário de tipo de gasto
    document.getElementById('addTipoForm').addEventListener('submit', handleAddTipo);
    
    // Formulário de registro
    document.getElementById('addRegistroForm').addEventListener('submit', handleAddRegistro);
}

// Carregar tipos de gasto
async function loadTiposGasto() {
    try {
        const response = await fetch(`${API_BASE_URL}/tipos-gasto/`);
        if (!response.ok) throw new Error('Erro ao carregar tipos de gasto');
        
        tiposGasto = await response.json();
        renderTiposGasto();
        updateTipoSelect();
        
    } catch (error) {
        console.error('Erro ao carregar tipos de gasto:', error);
        throw error;
    }
}

// Carregar registros
async function loadRegistros() {
    try {
        const response = await fetch(`${API_BASE_URL}/registros/`);
        if (!response.ok) throw new Error('Erro ao carregar registros');
        
        registros = await response.json();
        renderRegistros();
        
    } catch (error) {
        console.error('Erro ao carregar registros:', error);
        throw error;
    }
}

// Renderizar tipos de gasto
function renderTiposGasto() {
    const container = document.getElementById('tipos-list');
    
    if (tiposGasto.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <i class="fas fa-tags"></i>
                <h3>Nenhum tipo de gasto encontrado</h3>
                <p>Comece criando seu primeiro tipo de gasto</p>
                <button class="btn btn-primary" onclick="showAddTipoModal()">
                    <i class="fas fa-plus"></i> Criar Primeiro Tipo
                </button>
            </div>
        `;
        return;
    }
    
    container.innerHTML = tiposGasto.map(tipo => `
        <div class="list-item">
            <div class="list-item-info">
                <div class="list-item-title">${tipo.descricao}</div>
                <div class="list-item-subtitle">
                    ${tipo.registros.length} registro(s) associado(s)
                </div>
            </div>
            <div class="list-item-actions">
                <button class="btn btn-sm btn-secondary" onclick="editTipo(${tipo.id})">
                    <i class="fas fa-edit"></i> Editar
                </button>
                <button class="btn btn-sm btn-danger" onclick="deleteTipo(${tipo.id})">
                    <i class="fas fa-trash"></i> Excluir
                </button>
            </div>
        </div>
    `).join('');
}

// Renderizar registros
function renderRegistros() {
    const container = document.getElementById('registros-list');
    
    if (registros.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <i class="fas fa-receipt"></i>
                <h3>Nenhum registro encontrado</h3>
                <p>Comece registrando seu primeiro gasto</p>
                <button class="btn btn-primary" onclick="showAddRegistroModal()">
                    <i class="fas fa-plus"></i> Registrar Primeiro Gasto
                </button>
            </div>
        `;
        return;
    }
    
    container.innerHTML = registros.map(registro => {
        const tipo = tiposGasto.find(t => t.id === registro.fk_tipo_gasto);
        const data = new Date(registro.dt_hr_gasto).toLocaleDateString('pt-BR');
        
        return `
            <div class="list-item">
                <div class="list-item-info">
                    <div class="list-item-title">R$ ${registro.vlr_gasto.toFixed(2)}</div>
                    <div class="list-item-subtitle">
                        ${tipo ? tipo.descricao : 'Tipo não encontrado'} • ${data}
                        ${registro.observacao ? ` • ${registro.observacao}` : ''}
                    </div>
                </div>
                <div class="list-item-actions">
                    <button class="btn btn-sm btn-secondary" onclick="editRegistro(${registro.id})">
                        <i class="fas fa-edit"></i> Editar
                    </button>
                    <button class="btn btn-sm btn-danger" onclick="deleteRegistro(${registro.id})">
                        <i class="fas fa-trash"></i> Excluir
                    </button>
                </div>
            </div>
        `;
    }).join('');
}

// Atualizar dashboard
function updateDashboard() {
    // Total de gastos
    const totalGastos = registros.reduce((sum, registro) => sum + registro.vlr_gasto, 0);
    document.getElementById('total-gastos').textContent = `R$ ${totalGastos.toFixed(2)}`;
    
    // Total de tipos
    document.getElementById('total-tipos').textContent = tiposGasto.length;
    
    // Total de registros
    document.getElementById('total-registros').textContent = registros.length;
    
    // Últimos gastos
    updateUltimosGastos();
}

// Atualizar últimos gastos
function updateUltimosGastos() {
    const container = document.getElementById('ultimos-gastos');
    const ultimosRegistros = registros
        .sort((a, b) => new Date(b.dt_hr_gasto) - new Date(a.dt_hr_gasto))
        .slice(0, 5);
    
    if (ultimosRegistros.length === 0) {
        container.innerHTML = '<p>Nenhum gasto registrado ainda</p>';
        return;
    }
    
    container.innerHTML = ultimosRegistros.map(registro => {
        const tipo = tiposGasto.find(t => t.id === registro.fk_tipo_gasto);
        const data = new Date(registro.dt_hr_gasto).toLocaleDateString('pt-BR');
        
        return `
            <div class="gasto-item">
                <div class="gasto-info">
                    <div class="gasto-valor">R$ ${registro.vlr_gasto.toFixed(2)}</div>
                    <div class="gasto-tipo">
                        ${tipo ? tipo.descricao : 'Tipo não encontrado'} • ${data}
                    </div>
                </div>
            </div>
        `;
    }).join('');
}

// Atualizar select de tipos
function updateTipoSelect() {
    const select = document.getElementById('registroTipo');
    select.innerHTML = '<option value="">Selecione um tipo...</option>' +
        tiposGasto.map(tipo => 
            `<option value="${tipo.id}">${tipo.descricao}</option>`
        ).join('');
}

// Mostrar modal de adicionar tipo
function showAddTipoModal() {
    document.getElementById('addTipoModal').style.display = 'block';
    document.getElementById('tipoDescricao').focus();
}

// Mostrar modal de adicionar registro
function showAddRegistroModal() {
    if (tiposGasto.length === 0) {
        showToast('Crie pelo menos um tipo de gasto primeiro!', 'warning');
        return;
    }
    
    document.getElementById('addRegistroModal').style.display = 'block';
    document.getElementById('registroValor').focus();
}

// Fechar modal
function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
    
    // Limpar formulários
    if (modalId === 'addTipoModal') {
        document.getElementById('addTipoForm').reset();
    } else if (modalId === 'addRegistroModal') {
        document.getElementById('addRegistroForm').reset();
    }
}

// Fechar modal ao clicar fora
window.onclick = function(event) {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
}

// Adicionar tipo de gasto
async function handleAddTipo(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);
    const data = {
        descricao: formData.get('descricao')
    };
    
    showLoading();
    
    try {
        const response = await fetch(`${API_BASE_URL}/tipos-gasto/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Erro ao criar tipo de gasto');
        }
        
        await loadTiposGasto();
        updateDashboard();
        closeModal('addTipoModal');
        showToast('Tipo de gasto criado com sucesso!', 'success');
        
    } catch (error) {
        showToast('Erro: ' + error.message, 'error');
        console.error('Erro ao criar tipo:', error);
    } finally {
        hideLoading();
    }
}

// Adicionar registro
async function handleAddRegistro(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);
    const data = {
        vlr_gasto: parseFloat(formData.get('vlr_gasto')),
        fk_tipo_gasto: parseInt(formData.get('fk_tipo_gasto')),
        observacao: formData.get('observacao') || null
    };
    
    showLoading();
    
    try {
        const response = await fetch(`${API_BASE_URL}/registros/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Erro ao criar registro');
        }
        
        await loadRegistros();
        updateDashboard();
        closeModal('addRegistroModal');
        showToast('Registro criado com sucesso!', 'success');
        
    } catch (error) {
        showToast('Erro: ' + error.message, 'error');
        console.error('Erro ao criar registro:', error);
    } finally {
        hideLoading();
    }
}

// Editar tipo de gasto
async function editTipo(id) {
    const tipo = tiposGasto.find(t => t.id === id);
    if (!tipo) return;
    
    const novaDescricao = prompt('Nova descrição:', tipo.descricao);
    if (!novaDescricao || novaDescricao === tipo.descricao) return;
    
    showLoading();
    
    try {
        const response = await fetch(`${API_BASE_URL}/tipos-gasto/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ descricao: novaDescricao })
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Erro ao atualizar tipo');
        }
        
        await loadTiposGasto();
        updateDashboard();
        showToast('Tipo de gasto atualizado!', 'success');
        
    } catch (error) {
        showToast('Erro: ' + error.message, 'error');
        console.error('Erro ao editar tipo:', error);
    } finally {
        hideLoading();
    }
}

// Excluir tipo de gasto
async function deleteTipo(id) {
    const tipo = tiposGasto.find(t => t.id === id);
    if (!tipo) return;
    
    if (!confirm(`Tem certeza que deseja excluir o tipo "${tipo.descricao}"?`)) {
        return;
    }
    
    showLoading();
    
    try {
        const response = await fetch(`${API_BASE_URL}/tipos-gasto/${id}`, {
            method: 'DELETE'
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Erro ao excluir tipo');
        }
        
        await Promise.all([loadTiposGasto(), loadRegistros()]);
        updateDashboard();
        showToast('Tipo de gasto excluído!', 'success');
        
    } catch (error) {
        showToast('Erro: ' + error.message, 'error');
        console.error('Erro ao excluir tipo:', error);
    } finally {
        hideLoading();
    }
}

// Editar registro
async function editRegistro(id) {
    const registro = registros.find(r => r.id === id);
    if (!registro) return;
    
    const novoValor = prompt('Novo valor (R$):', registro.vlr_gasto);
    if (!novoValor || parseFloat(novoValor) === registro.vlr_gasto) return;
    
    showLoading();
    
    try {
        const response = await fetch(`${API_BASE_URL}/registros/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ vlr_gasto: parseFloat(novoValor) })
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Erro ao atualizar registro');
        }
        
        await loadRegistros();
        updateDashboard();
        showToast('Registro atualizado!', 'success');
        
    } catch (error) {
        showToast('Erro: ' + error.message, 'error');
        console.error('Erro ao editar registro:', error);
    } finally {
        hideLoading();
    }
}

// Excluir registro
async function deleteRegistro(id) {
    const registro = registros.find(r => r.id === id);
    if (!registro) return;
    
    if (!confirm(`Tem certeza que deseja excluir este registro de R$ ${registro.vlr_gasto.toFixed(2)}?`)) {
        return;
    }
    
    showLoading();
    
    try {
        const response = await fetch(`${API_BASE_URL}/registros/${id}`, {
            method: 'DELETE'
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Erro ao excluir registro');
        }
        
        await loadRegistros();
        updateDashboard();
        showToast('Registro excluído!', 'success');
        
    } catch (error) {
        showToast('Erro: ' + error.message, 'error');
        console.error('Erro ao excluir registro:', error);
    } finally {
        hideLoading();
    }
}

// Mostrar loading
function showLoading() {
    document.getElementById('loading').style.display = 'block';
}

// Esconder loading
function hideLoading() {
    document.getElementById('loading').style.display = 'none';
}

// Mostrar toast
function showToast(message, type = 'success') {
    const container = document.getElementById('toast-container');
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;
    
    container.appendChild(toast);
    
    // Remover toast após 3 segundos
    setTimeout(() => {
        toast.remove();
    }, 3000);
}
