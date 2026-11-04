from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import get_settings

settings = get_settings()

engine = create_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    """Base class for all models (app/models)."""


def get_db():
    """Dependencia do FastAPI: abre e fecha a sessao a cada requisicao."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()