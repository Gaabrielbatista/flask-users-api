# API Flask de Aprendizado

Pequena API de exemplo construída com Flask para fins de estudo e demonstração.

## Descrição

Projeto simples que expõe uma lista de carros em memória e permite adicionar novos registros via JSON.

Principais funcionalidades:
- Página inicial em HTML (`/`) com links para testar a API.
- Endpoint `GET /carros` — retorna a lista de carros em JSON.
- Endpoint `POST /carros` — cadastra um novo carro (envie JSON com pelo menos `id`, `marca`, `modelo`).

OBS: Os dados atuais são armazenados na lista `Carros` em memória (`app/bd.py`).

## Estrutura do projeto

- `app/` — código da aplicação Flask
  - `app.py` — aplicação Flask principal
  - `bd.py` — base de dados em memória (lista `Carros`)
- `templates/` — templates HTML (`index.html`, `carro_form.html`)
- `db/CreateDatabase.sql` — script de exemplo para criar uma tabela MySQL
- `Dockerfile`, `docker-compose.yml` — arquivos para rodar em Docker
- `requirements.txt` — dependências (para ambiente local)

## Requisitos

- Python 3.10+ (ou use Docker)
- pip (se executar localmente)

## Executando localmente

1. Instale dependências:

```bash
pip install -r requirements.txt
```

2. Execute a aplicação (a partir da raiz do projeto):

```bash
python app/app.py
```

3. Acesse no navegador: `http://localhost:5000`

## Executando com Docker

Crie um arquivo `.env` com as variáveis de ambiente do MySQL (exemplo):

```env
MYSQL_DATABASE=gaabrielDB
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
Se quiser, adiciono: testes automatizados, rota `GET /carros/novo`, ou integração com MySQL.
