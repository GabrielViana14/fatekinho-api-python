"""
# Fatekinho API - Python/FastAPI

Este projeto é uma API desenvolvida com [FastAPI](https://fastapi.tiangolo.com/), oferecendo várias rotas para gerenciar clientes, usuários, autenticação e histórico de vitórias/derrotas.

---

## 🚀 Começando

Estas instruções irão ajudá-lo a configurar e rodar o projeto localmente.

### Pré-requisitos

Certifique-se de ter instalado:
- Python 3.10 ou superior
- Gerenciador de pacotes `pip`

### 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/GabrielViana14/fatekinho-api-python
   cd fatekinho-api-python
   
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate      # Linux/MacOS
    venv\Scripts\activate         # Windows
    
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
   
### 🔧 Como rodar o projeto
#### Rodar localmente
1. Para iniciar a API localmente, execute o seguinte comando:
    ```bash
    uvicorn main:app --reload

A API estará disponível em: http://127.0.0.1:8000/docs

#### Rodar no GitHub Codespace
1. Para rodar no GitHub Codespace:
    ```bash
    python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
A API estará disponível em: http://<seu-codespace-url>:8000/docs

### 📖 Documentação da API
A FastAPI gera automaticamente uma documentação interativa acessível no endpoint /docs:<br>
Local: http://127.0.0.1:8000/docs<br>
Outra URL: Adicione /docs ao final da URL.<br>

### 🛠️ Estrutura do Projeto
    ├── main.py                   # Arquivo principal que inicializa a API
    ├── config/                   # Diretório com as configurações da API
    │   ├── auth.py               # Geração e verificação de tokens
    │   └── config.py             # hyper paraments da API
    ├── database/                 # Diretório com dados para conexão ao banco de dados online
    │   └── database.py           # conexão ao banco de dados
    ├── models/                   # Modelos de dados para retorno das rotas
    │   ├── histWonLose.py        # Modelo para rota histórico de vitórias/derrotas
    │   ├── login.py              # Modelo para rota de login
    │   ├── tabelaCombinada.py    # Modelo para rota de tabelaCombinada
    │   ├── token.py              # Modelo para geração de token
    │   └── usuarios.py           # Modelo para rota de usuarios
    ├── rotas/                    # Diretório com as rotas da aplicação
    │   ├── usuarios.py           # Rotas relacionadas aos usuários
    │   ├── autenticacao.py       # Rotas para autenticação
    │   ├── historicoWonLose.py   # Rotas para histórico de vitórias/derrotas
    │   └── tabelaCombinada.py    # Rotas para dados da operações feitas pelo usuário
    ├── requirements.txt          # Dependências do projeto
    └── README.md                 # Documentação do projeto

### 🧪 Testando a API
Para testar as rotas da API, você pode:
- Usar a documentação interativa: http://127.0.0.1:8000/docs<br>
- Utilizar ferramentas como Postman ou curl.<br>

### ✨ Rotas Implementadas
Rota Principal
GET /
- Retorna uma mensagem de status:
    ```json
    "API rodando"
- Rotas Importadas
  - Usuários: /usuarios
  - Autenticação: /auth
  - Histórico de Vitórias/Derrotas: /historico-won-lose
  - Tabelas Combinadas: /table-comb

### 🛠 Tecnologias Utilizadas
- FastAPI: Framework para construir APIs modernas e rápidas.
- Uvicorn: Servidor ASGI para rodar a aplicação.
- Python 3.10+

### 📜 Licença
  Este projeto é licenciado sob os termos da licença MIT.