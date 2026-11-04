# Quantum HidroSmart - Backend

API em FastAPI + PostgreSQL (SQLAlchemy) com scikit-learn para o modelo preditivo.

## Estrutura

```
app/
  main.py        # criacao do app, CORS e routers
  core/          # config (.env) e conexao com o banco
  routers/       # endpoints (um arquivo por recurso)
  models/        # tabelas SQLAlchemy
  schemas/       # schemas Pydantic (entrada/saida)
  services/      # regras de negocio e ML
tests/
```

## Como rodar

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # ajuste DATABASE_URL
uvicorn app.main:app --reload
```

- API: http://localhost:8000
- Docs (Swagger): http://localhost:8000/docs
- Health check: http://localhost:8000/health

## Testes

```bash
pytest
```

## Convencao de branches

`main` (estavel) <- `develop` <- `feature/nome-da-task`