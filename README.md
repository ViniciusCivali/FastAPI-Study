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