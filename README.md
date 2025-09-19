# FastAPI-Study
Study FastAPI 

# Setup repo
it clone git@github.com-personal:ViniciusCivali/FastAPI-Study.git
cd FastAPI-Study

# Init
poetry init
poetry config virtualenvs.in-project true
poetry env use python3.13
poetry add fastapi
poetry add uvicorn[standard]
poetry add --group dev black ruff pytest pre-commit

# Server
poetry run uvicorn main:app --reload

Acess: http://127.0.0.1:8000
Automatic documentation: http://127.0.0.1:8000/docs

# Docker
docker build -t fastapi .
docker run --rm -it -p 8000:8000 fastapi bash
uvicorn main:app --host 0.0.0.0 --port 8000

# Docker compose
docekr compose up --build

