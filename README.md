# 📦 Sistema de Gestão de Estoque

## 📖 Descrição
Sistema profissional de gestão de estoque desenvolvido em Python, usando arquitetura MVC (Model-View-Controller). Este repositório foi migrado para usar MongoDB como banco de dados principal (coleções: `Fornecedores`, `Produtos`, `Compras`) — há também um utilitário para migrar dados de MySQL, caso você esteja atualizando de uma versão antiga.

## ✨ Funcionalidades

### 📊 Dashboard e Controle
- Visão geral do estoque com totais e valores em tempo real
- Monitoramento de produtos com estoque baixo
- Acompanhamento do valor total do estoque
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

### Requisitos Gerais
1. **Python 3.8+**
2. **MongoDB** (local ou em nuvem — MongoDB Atlas)
3. **(Opcional) MySQL 8.0+** — apenas se você precisar migrar dados antigos
4. **Pip** (gerenciador de pacotes Python)

### Windows
1. **Instalar Python 3.8+**
   ```powershell
   python --version
   # Se necessário: https://www.python.org/downloads/windows/
   ```

2. **Instalar MongoDB** (Community Server ou usar Atlas):
   - Para local: baixe o instalador em https://www.mongodb.com/try/download/community e siga as instruções.
   - Ou opte por MongoDB Atlas e crie um cluster gratuito.

3. **Dependências Python**
   ```powershell
   python -m pip install --upgrade pip
   pip install pymongo mysql-connector-python python-dotenv
   ```

### Linux (Ubuntu/Debian)
1. **Python 3.8+**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip -y
   ```

2. **MongoDB**
   ```bash
   # Usando pacotes oficiais do Ubuntu/Debian
   sudo apt install -y mongodb
   sudo systemctl start mongodb
   sudo systemctl enable mongodb
   sudo systemctl status mongodb
   ```

3. **Dependências Python**
   ```bash
   python3 -m pip install --upgrade pip
   pip3 install pymongo mysql-connector-python python-dotenv
   ```

## 🚀 Instalação e Configuração

1. **Clonar o Repositório**
   ```bash
   git clone https://github.com/DricoFerr/SistemaDeEstoque.git
   cd SistemaDeEstoque
   ```

2. **Popular / Inicializar o MongoDB**
   - O repositório contém `init_mongo.js` com dados de exemplo. Para importar o arquivo no MongoDB local (ou em um shell remoto), rode:
     ```bash
     # Usando mongosh (recomendado):
     mongosh --file init_mongo.js
     ```
   - Se estiver usando Atlas, valide a string de conexão e importe via mongosh apontando para o cluster.

3. **Executar Migração (opcional — MySQL -> MongoDB)**
   - Se você já possui dados em MySQL, use `migracao.py` para migrar tabelas `fornecedores` e `produtos` para o MongoDB.
   - Configure as credenciais MySQL dentro do `migracao.py` ou em um `.env` (caso use `python-dotenv`), depois execute:
     ```bash
     python migracao.py
     ```

4. **Configurar Conexão**
   - O arquivo `conexion.py` conecta-se por padrão em `mongodb://localhost:27017/` e usa a database `estoque`.
   - Para usar outro endereço (por exemplo Atlas): abra `conexion.py` e altere a string de conexão.

5. **Executar o Sistema (CLI)**
   ```bash
   # Windows
   python main.py

   # Linux
   python3 main.py
   ```

## 🧰 Dependências (Python)
- pymongo — driver MongoDB
- mysql-connector-python — somente necessário para `migracao.py` (caso migre do MySQL)
- python-dotenv — opcional, para configuração via `.env`

Instale todas com:
```bash
# Windows
python -m pip install --upgrade pip
pip install pymongo mysql-connector-python python-dotenv

# Linux
python3 -m pip install --upgrade pip
pip3 install pymongo mysql-connector-python python-dotenv
```

## 🎯 Guia Rápido de Uso

1. **Primeiro Acesso**
   - Execute o sistema com `python main.py`
   - Observe o splash screen com totais
   - Navegue pelo menu CLI

2. **Iniciar Cadastros**
   - Controles recomendados: cadastrar primeiro fornecedores, depois produtos e então registrar compras.

3. **Gerenciar Estoque**
   - Use os relatórios e o dashboard para monitorar produtos abaixo do estoque mínimo e gerar pedidos de reposição.

## 📂 Estrutura do Projeto
```
SistemaDeEstoque/
├── controller/           # Lógica de negócios (Controllers)
├── model/                # Entidades do sistema
├── utils/                # Utilidades e interface (CLI)
├── init_mongo.js         # Script para popular o MongoDB com dados de exemplo
├── conexion.py           # Conexão com MongoDB
├── migracao.py           # Script opcional para migrar MySQL -> MongoDB
├── main.py               # Ponto de entrada do CLI
├── estoque.sql           # Script SQL (MySQL) usado apenas para referência / migração
└── README.md
```

## 💡 Dicas e Observações
- Se estiver usando MongoDB Atlas, atualize a string de conexão em `conexion.py`.
- Para testes locais, `mongosh --file init_mongo.js` popula o banco com dados de amostra (Fornecedores, Produtos, Compras).
- Utilize `migracao.py` apenas uma vez, pois ele limpa as coleções antes de inserir — tome backup do seu banco caso necessário.
- Se ocorrerem erros de conexão, valide se o serviço do MongoDB está em execução e a porta 27017 está aceitando conexões.

## 👥 Equipe de Desenvolvimento
- **Adriano Ferraz Guimarães**
- **Filippo Salles Morais**
- **Mário Márcio Holsbach**
- **Matheus Marmo Sorio**
- **Ricardo Vasconcellos Drumond**

## 📄 Link do video tutorial
https://youtu.be/az7zzplQha8
