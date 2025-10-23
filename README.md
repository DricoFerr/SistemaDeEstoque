# Sistema de Gestão de Estoque

## 📖 Descrição
Este é um sistema de linha de comando (CLI) para gestão de estoque, desenvolvido como projeto para a disciplina de Banco de Dados. A aplicação permite o controle completo de produtos, fornecedores e compras, utilizando uma arquitetura organizada em camadas (Model-Controller-View) para separar as responsabilidades.

---

## ✨ Funcionalidades Principais
- **Gestão de Produtos:**
  - Adicionar novos produtos.
  - Listar todos os produtos cadastrados.
  - Atualizar informações de um produto.
  - Remover produtos (com validação para impedir a exclusão de itens associados a compras).

- **Gestão de Fornecedores:**
  - Adicionar novos fornecedores.
  - Listar, atualizar e remover fornecedores existentes.

- **Registro de Compras:**
  - Registrar novas compras de produtos.
  - Atualização automática do estoque do produto após cada compra registrada.

- **Relatórios:**
  - **Sumarização:** Exibe o total de compras e o valor gasto, agrupados por fornecedor.
  - **Junção:** Mostra um relatório detalhado de todas as compras, com informações do produto e do fornecedor.
  - **Estoque Baixo:** Lista todos os produtos que precisam de reposição (quantidade atual abaixo do estoque mínimo).

- **Interface de Usuário:**
  - Tela de abertura (*Splash Screen*) com um resumo dos registros no banco de dados.
  - Menus interativos e de fácil navegação para acessar todas as funcionalidades.

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3
- **Banco de Dados:** MySQL
- **Biblioteca de Conexão:** `mysql-connector-python`

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.x instalado.
- Servidor MySQL em execução.
- A biblioteca `mysql-connector-python`.

### 1. Instalação
Clone o repositório para sua máquina local:
```bash
git clone <URL_DO_REPOSITORIO>
cd SistemaDeEstoque
```

Instale a dependência necessária:
```bash
pip install mysql-connector-python
```

### 2. Configuração do Banco de Dados
1. Crie um banco de dados no seu servidor MySQL com o nome `estoque`.
2. Execute o script `estoque.sql` para criar as tabelas e popular os dados iniciais.
3. Abra o arquivo `conexion.py` e atualize as credenciais de conexão com o seu banco de dados (usuário, senha, host).

### 3. Execução
Para iniciar o sistema, execute o arquivo `main.py` a partir do diretório raiz do projeto. O comando é o mesmo para Windows, macOS e Linux:
```bash
python3 main.py
```

---

## 📁 Estrutura do Projeto
O projeto segue uma arquitetura que separa as responsabilidades em diferentes pastas:
- `model/`: Contém as classes que representam as entidades do banco de dados (`Produto`, `Fornecedor`, `Compra`).
- `controller/`: Responsável pela lógica de negócio e pela comunicação entre os menus e o banco de dados.
- `utils/`: Contém os módulos de interface com o usuário (`menus.py`), tela de abertura (`splash_screen.py`) e funções auxiliares (`helpers.py`).
- `main.py`: Ponto de entrada da aplicação.
- `conexion.py`: Gerencia a conexão com o banco de dados MySQL.
- `estoque.sql`: Script para criação e população do banco de dados.

---

## 👨‍💻 Autores
- Adriano Ferraz Guimarães
- Ricardo Vasconcellos 