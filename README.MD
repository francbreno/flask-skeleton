Preparar aplicação
===

1. Criar ambiente virtual (venv):

python3 -m venv venv
source venv/bin/activate

2. Atualizar o 'pip':

pip install --upgrade pip

3. Instalar as dependências do projeto

pip install -r requirements.txt

4. Criar repositório de migrations:

./run.py db init

5. Criar os script de migrations: (precisa do banco rodando: docker-compose up)

./run.py db migrate -m "primeira migration"

6. Aplicar o upgrade da migration

./run.py db upgrade
