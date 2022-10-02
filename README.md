# API TCC

API para consulta e cadastro de informações.

-- -

### 📋 Pré-requisitos

1 - Instalar Poetry:

https://python-poetry.org/docs/#installation
 
2 - Permitir criação virtual env local

```
poetry config virtualenvs.in-project true
```

3 - Criação virtual env

```
poetry shell
```

-- -

### 🔧 Instalação 
Instalação dependencias

```
poetry install
```

-- -

### 🔧 Execução

📋 **CLI (Command-line Interface)**

```
poetry run api
```

📋 **Docker**

Adicionar as variaveis de ambiente antes da execução

```
docker-compose -f local.yml up --build
```

-- -

### 📋 Requisições

Pesquisar status de erro do envio SMS no MongoDB a partir do ID_MO

```
curl --request GET 'http://localhost:7000/mongo/error/15851959872'
```

Pesquisar status do envio SMS no MySQL a partir do ID_MO

```
curl --location --request GET 'http://localhost:7000/mysql/status/15851959872'
```

-- -

### 🔧 Deploy

utilizar o commitzen para commit

```
git add .

cz commit

git push origin master
```

-- -

## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [fastapi](https://fastapi.tiangolo.com/) - FastAPI framework

-- -

## 🛠 TODO

**- Criar CI/CD**

**- Atualizar Docstrings**

-- -

## ✒️ Autores

* **Victor Augusto Barros** - - [VictorAugustoBarros](https://github.com/VictorAugustoBarros)
