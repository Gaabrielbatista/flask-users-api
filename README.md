# API Flask - Gerenciamento de Usuários

API RESTful desenvolvida com Flask para fins de aprendizado e demonstração de conceitos fundamentais de desenvolvimento backend. Permite o gerenciamento completo de usuários (CRUD) utilizando MySQL como banco de dados.

## 📋 Descrição

Projeto educacional que implementa operações CRUD (Create, Read, Update, Delete) em usuários. Desenvolvido como parte do aprendizado em desenvolvimento de APIs com Python e Flask, demonstrando boas práticas como estruturação de código, validação de dados, conexão com banco de dados e deploy com Docker.

## 🚀 Funcionalidades

- **Listar usuários**: Recupera todos os usuários cadastrados
- **Buscar usuário por ID**: Obtém detalhes de um usuário específico
- **Criar usuário**: Adiciona um novo usuário ao sistema
- **Atualizar usuário**: Modifica informações de um usuário existente
- **Excluir usuário**: Remove um usuário do sistema
- **CORS habilitado**: Permite requisições de diferentes origens

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Flask**: Framework web para Python
- **Flask-CORS**: Suporte a CORS
- **MySQL**: Banco de dados relacional
- **mysql-connector-python**: Conector MySQL para Python
- **python-dotenv**: Gerenciamento de variáveis de ambiente
- **Docker & Docker Compose**: Containerização e orquestração

## 📁 Estrutura do Projeto

```
project/
│
├── app.py
│
├── database/
│   └── connection.py
│
├── routes/
│   └── user_routes.py
│
├── models/
│   └── user_model.py
│
└── validators/
    └── user_validator.py
```

## 📖 Endpoints da API

| Método | Endpoint       | Descrição                    |
|--------|----------------|------------------------------|
| GET    | `/users`       | Lista todos os usuários      |
| GET    | `/users/<id>`  | Busca usuário por ID         |
| POST   | `/users`       | Cria um novo usuário         |
| PUT    | `/users/<id>`  | Atualiza usuário existente   |
| DELETE | `/users/<id>`  | Exclui usuário               |

### Exemplo de Payload (POST/PUT)

```json
{
  "nome": "João Silva",
  "email": "joao@email.com",
  "idade": 30
}
```

## 🗄️ Banco de Dados

A aplicação utiliza MySQL com a seguinte estrutura de tabela:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    idade INT NOT NULL
);
```

## ⚙️ Instalação e Execução

### Pré-requisitos

- Python 3.10+
- Docker e Docker Compose (opcional, mas recomendado)

### Executando Localmente

1. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure as variáveis de ambiente** — crie um arquivo `.env` na raiz do projeto:
   ```env
   MYSQL_USER=seu_usuario
   MYSQL_PASSWORD=sua_senha
   MYSQL_HOST=localhost
   MYSQL_DATABASE=nome_do_banco
   MYSQL_ROOT_PASSWORD=senha_root
   ```

3. **Crie o banco de dados** executando o script `CreateDatabase.sql` no seu MySQL.

4. **Inicie a aplicação**:
   ```bash
   python app.py
   ```

5. **Acesse a API** em `http://localhost:5000`.

### Executando com Docker

1. **Configure o arquivo `.env`** (como acima).

2. **Suba os containers**:
   ```bash
   docker-compose up --build
   ```

3. **Acesse a API** em `http://localhost:5000`.

### Exemplos de Uso

```bash
# Listar usuários
curl http://localhost:5000/users

# Criar usuário
curl -X POST http://localhost:5000/users \
  -H 'Content-Type: application/json' \
  -d '{"nome": "João Silva", "email": "joao@email.com", "idade": 30}'

# Atualizar usuário
curl -X PUT http://localhost:5000/users/1 \
  -H 'Content-Type: application/json' \
  -d '{"nome": "João Souza", "email": "joao@email.com", "idade": 31}'

# Excluir usuário
curl -X DELETE http://localhost:5000/users/1
```

## 📝 Conceitos Abordados

- Estruturação de APIs RESTful
- Conexão e operações com banco de dados MySQL
- Tratamento de requisições HTTP
- Validação de dados
- Gerenciamento de variáveis de ambiente com `.env`
- Containerização com Docker
- Boas práticas de desenvolvimento Python

## 🤝 Contribuição

Este é um projeto de aprendizado pessoal. Sugestões e melhorias são bem-vindas!

## 📄 Licença

Projeto para fins educacionais — sem licença específica.
