# Car API

API REST desenvolvida em Python com [FastAPI](https://fastapi.tiangolo.com/) e gerenciada via [Poetry](https://python-poetry.org/).

---

## 📋 Pré-requisitos

- **Python**: `>= 3.12`
- **Poetry**: `>= 2.0` (certifique-se de que o Poetry esteja instalado e no seu `PATH`, ex: `~/.local/bin`)

---

## 🚀 Instalação e Execução

### 1. Clonar ou Acessar o Repositório

```bash
cd /caminho/para/car_api
```

### 2. Instalar as Dependências

Execute o comando abaixo para instalar todas as dependências declaradas no `poetry.lock`:

```bash
poetry install
```

---

## ⚡ Ativação do Ambiente Virtual

Você tem duas formas principais de interagir com o ambiente virtual do Poetry:

### Opção A: Ativar o shell do ambiente virtual

Para entrar diretamente na sessão do shell com o ambiente virtual ativado:

```bash
poetry shell
```

Ou utilizando o comando de ativação do Poetry:

```bash
source $(poetry env info --path)/bin/activate
# ou no Poetry 2+:
eval $(poetry env activate)
```

> **Para desativar**: basta digitar `deactivate` (se usou `source`) ou `exit` (se usou `poetry shell`).

### Opção B: Executar comandos diretamente com `poetry run`

Se preferir não ativar explicitamente o shell interativo, você pode rodar qualquer comando prefixando com `poetry run`:

```bash
poetry run <comando>
```

---

## 💻 Subir a Aplicação Localmente

Com o ambiente ativado (ou usando `poetry run`), inicie o servidor de desenvolvimento:

### Utilizando FastAPI CLI (Recomendado)

```bash
# Se o ambiente virtual estiver ativado:
fastapi dev car_api/app.py

# Ou diretamente via Poetry:
poetry run fastapi dev car_api/app.py
```

### Alternativa utilizando Uvicorn diretamente

```bash
# Se o ambiente virtual estiver ativado:
uvicorn car_api.app:app --reload

# Ou diretamente via Poetry:
poetry run uvicorn car_api.app:app --reload
```

O servidor será inicializado por padrão no endereço: **http://127.0.0.1:8000**

---

## 📖 Documentação Interativa & Endpoints

Com a aplicação em execução, acesse a documentação interativa pelo navegador:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Endpoints Principais:

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/health_check` | Verifica a saúde da aplicação (`{"status": "OK"}`) |
| `GET` | `/api/v1/users/` | Retorna a lista de usuários cadastrados |
| `POST` | `/api/v1/users/` | Cria um novo usuário |

### Gerar migrações com Alembic
- **Comando**: `poetry run alembic revision --autogenerate -m "<message>"`

### Aplicar migrações com Alembic
- **Comando**: `poetry run alembic upgrade head`
