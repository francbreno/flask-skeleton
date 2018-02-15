Um boilerplate para criação de aplicações com **Python 3** e **Flask**

## Dependências

* Flask-JWT 0.3.2
* flask-marshmallow 0.8.0
* Flask-Migrate 2.0.3
* Flask-RESTful 0.3.5
* Flask-Script 2.0.5
* Flask-SQLAlchemy 2.2

## Preparar aplicação

### 1. Criar ambiente virtual (venv)

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Atualizar o 'pip'

```bash
pip install --upgrade pip
```

### 3. Instalar as dependências do projeto

```bash
pip install -r requirements.txt
```

### 4. Criar repositório de migrations

```bash
./run.py db init
```

### 5. Criar os script de migrations

```bash
# subir o banco no docker
docker-compose up
./run.py db migrate -m "primeira migration"
```

### 6. Aplicar o upgrade da migration

```bash
./run.py db upgrade
```
