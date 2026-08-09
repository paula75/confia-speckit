"""SQLAlchemy engine and session factory for bw-backend's own PostgreSQL database.

Ver specs/001-gestion-integral-reservas/research.md §"Persistencia propia de BW (PostgreSQL)".
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ.get(
    "DATABASE_URL", "postgresql+psycopg://bw:bw@localhost:5432/bw"
)

engine = create_engine(DATABASE_URL, future=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


def get_db():
    """FastAPI dependency: yields a session, closing it after the request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
