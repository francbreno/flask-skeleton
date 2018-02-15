Preparar aplicação
===

## 1. Criar ambiente virtual (venv):

```bash
python3 -m venv venv
source venv/bin/activate
```

## 2. Atualizar o 'pip':

```bash
pip install --upgrade pip
```

## 3. Instalar as dependências do projeto

```bash
pip install -r requirements.txt
```

## 4. Criar repositório de migrations:

```bash
./run.py db init
```

## 5. Criar os script de migrations: (precisa do banco rodando: docker-compose up)

```bash
./run.py db migrate -m "primeira migration"
```

## 6. Aplicar o upgrade da migration

```bash
./run.py db upgrade
```
