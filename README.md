# 📦 Sistema de Gestão de Estoque

## 📖 Descrição
Sistema profissional de gestão de estoque desenvolvido em Python, utilizando arquitetura MVC (Model-View-Controller) e banco de dados MySQL. Oferece controle completo de produtos, fornecedores e compras através de uma interface de linha de comando (CLI) intuitiva e eficiente.

## ✨ Funcionalidades

### 📊 Dashboard e Controle
- Visão geral do estoque com totais e valores em tempo real
- Monitoramento de produtos com estoque baixo
- Acompanhamento de valor total do estoque
- Contadores de registros atualizados em tempo real

### 🏭 Gestão de Produtos
- Cadastro e manutenção de produtos
- Controle de estoque mínimo
- Atualização automática após compras
- Proteção contra exclusão de produtos vinculados

### 👥 Gestão de Fornecedores
- Cadastro completo de fornecedores
- Vinculação com produtos
- Dados de contato e endereço
- Controle de relacionamento produto-fornecedor

### 🛍️ Registro de Compras
- Entrada de mercadorias
- Atualização automática do estoque
- Cálculo automático de valores
- Histórico completo de transações

### 📈 Relatórios
- **Sumarização por Fornecedor:** Total de compras e valores
- **Relatório Detalhado:** Histórico completo de operações
- **Estoque Crítico:** Produtos que necessitam reposição

## 🛠️ Requisitos do Sistema

### Windows
1. **Python 3.8+**
   ```powershell
   # Verificar se já está instalado
   python --version
   
   # Se não estiver instalado, baixe do site oficial:
   # https://www.python.org/downloads/windows/
   ```

2. **MySQL 8.0+**
   ```powershell
   # Download do MySQL Installer:
   # https://dev.mysql.com/downloads/installer/
   
   # Após instalação, verificar serviço:
   Get-Service -Name "MySQL*"
   ```

3. **Dependências Python**
   ```powershell
   # Instalar gerenciador de pacotes
   python -m pip install --upgrade pip
   
   # Instalar conector MySQL
   pip install mysql-connector-python
   ```

### Linux (Ubuntu/Debian)
1. **Python 3.8+**
   ```bash
   # Atualizar repositórios
   sudo apt update
   
   # Instalar Python
   sudo apt install python3 python3-pip
   ```

2. **MySQL 8.0+**
   ```bash
   # Instalar MySQL
   sudo apt install mysql-server
   
   # Iniciar serviço
   sudo systemctl start mysql
   
   # Habilitar início automático
   sudo systemctl enable mysql
   ```

3. **Dependências Python**
   ```bash
   # Atualizar pip
   python3 -m pip install --upgrade pip
   
   # Instalar conector MySQL
   pip3 install mysql-connector-python
   ```

## 🚀 Instalação e Configuração

1. **Clonar o Repositório**
   ```bash
   git clone https://github.com/DricoFerr/SistemaDeEstoque.git
   cd SistemaDeEstoque
   ```

2. **Configurar Banco de Dados**
   ```bash
   # Windows (PowerShell como Administrador)
   mysql -u root -p < estoque.sql
   
   # Linux
   sudo mysql -u root -p < estoque.sql
   ```

3. **Configurar Conexão**
   - Abrir `conexion.py`
   - Ajustar credenciais:
     ```python
     host="localhost"
     user="seu_usuario"
     password="sua_senha"
     database="estoque"
     ```

4. **Executar o Sistema**
   ```bash
   # Windows
   python main.py
   
   # Linux
   python3 main.py
   ```

## 🎯 Guia Rápido de Uso

1. **Primeiro Acesso**
   - Execute o sistema
   - Observe o splash screen com totais
   - Use o menu principal para navegação

2. **Cadastros Básicos**
   - Comece cadastrando fornecedores
   - Depois cadastre os produtos
   - Vincule produtos aos fornecedores

3. **Operações Diárias**
   - Registre compras
   - Monitore o estoque
   - Consulte relatórios

4. **Manutenção**
   - Atualize cadastros quando necessário
   - Monitore produtos com estoque baixo
   - Faça backup do banco regularmente

## 📂 Estrutura do Projeto
```
SistemaDeEstoque/
├── controller/           # Lógica de negócios
├── model/               # Entidades do sistema
├── utils/               # Utilitários e interface
├── conexion.py          # Conexão com banco
├── main.py             # Ponto de entrada
├── estoque.sql         # Script do banco
└── README.md           # Documentação
```

## 👥 Equipe de Desenvolvimento
- **Adriano Ferraz Guimarães**

- **Filippo Salles Morais**

- **Mário Márcio Holsbach**

- **Ricardo Vasconcellos Drumond**

## 📄 Link do video tutorial:
https://youtu.be/az7zzplQha8
