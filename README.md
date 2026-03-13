# API Flask de Aprendizado - Gerenciamento de Usuários

Este é um projeto de API RESTful desenvolvida com Flask para fins de aprendizado e demonstração de conceitos fundamentais de desenvolvimento backend. A API permite o gerenciamento completo de usuários (CRUD) utilizando MySQL como banco de dados.

## 📋 Descrição

Projeto educacional que implementa uma API simples para operações CRUD (Create, Read, Update, Delete) em usuários. Desenvolvido como parte do aprendizado em desenvolvimento de APIs com Python e Flask, demonstrando boas práticas como estruturação de código, validação de dados, conexão com banco de dados e deploy com Docker.

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
| GET    | `/users`      | Lista todos os usuários     |
| GET    | `/users/<id>` | Busca usuário por ID        |
| POST   | `/users`      | Cria um novo usuário        |
| PUT    | `/users/<id>` | Atualiza usuário existente  |
| DELETE | `/users/<id>` | Exclui usuário              |

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

1. **Clone o repositório** (se aplicável)

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure o banco de dados**:
   - Crie um arquivo `.env` com as variáveis de ambiente:
     ```
     MYSQL_USER=seu_usuario
     MYSQL_PASSWORD=sua_senha
     MYSQL_HOST=localhost
     MYSQL_DATABASE=nome_do_banco
     MYSQL_ROOT_PASSWORD=senha_root
     ```

4. **Execute o script de criação do banco**:
   ```bash
   # Execute o CreateDatabase.sql no seu MySQL
   ```

5. **Execute a aplicação**:
   ```bash
   python app/app.py
   ```

6. **Acesse a API**:
   - URL: `http://localhost:5000`

### Executando com Docker

1. **Configure o arquivo `.env`** (como acima)

2. **Execute com Docker Compose**:
   ```bash
   docker-compose up --build
   ```

3. **Acesse a API**:
   - URL: `http://localhost:5000`

## 📝 Notas de Aprendizado

Este projeto foi desenvolvido com foco em aprendizado, abordando conceitos como:

- Estruturação de APIs RESTful
- Conexão e operações com banco de dados MySQL
- Tratamento de requisições HTTP
- Validação de dados
- Gerenciamento de variáveis de ambiente
- Containerização com Docker
- Boas práticas de desenvolvimento Python

## 🤝 Contribuição

Este é um projeto de aprendizado pessoal. Sugestões e melhorias são bem-vindas!

## 📄 Licença

Este projeto é para fins educacionais e não possui licença específica.

```env
MYSQL_DATABASE=bancodados
MYSQL_ROOT_PASSWORD=secret
MYSQL_USER=usuario
MYSQL_PASSWORD=senha
MYSQL_HOST=db
```

Em seguida execute:

```bash
docker-compose up --build
```

A aplicação ficará disponível em `http://localhost:5000`.

## Endpoints / Exemplos

- Listar carros:

```bash
curl http://localhost:5000/carros
```

- Cadastrar carro (JSON):

```bash
curl -X POST http://localhost:5000/carros \
  -H 'Content-Type: application/json' \
  -d '{"id":6, "marca":"Toyota", "modelo":"Corolla", "ano":2010}'
```

## Observações e TODOs

- O projeto usa uma lista em memória (`app/bd.py`) como fonte de dados. Para persistência, importe `db/CreateDatabase.sql` em um MySQL e adapte `app.py` para usar um cliente de BD.
- O template `carro_form.html` existe, mas não há rota explícita `GET /carros/novo` implementada em `app/app.py`. Se desejar, posso adicionar essa rota para renderizar o formulário.
- O `Dockerfile` atual executa `python app.py` no diretório `/app`; dependendo do contexto de cópia, pode ser necessário ajustar o `CMD` para `python app/app.py`.

## Licença

Projeto de aprendizado — sem licença definida.

---
