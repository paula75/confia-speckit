"""Fixture de sesión aislada de base de datos por test.

Ver specs/001-gestion-integral-reservas/research.md §"Estrategia de aislamiento de
base de datos en pruebas": cada test que ejercita un servicio contra PostgreSQL
corre dentro de una transacción SQLAlchemy propia, abierta aquí y revertida
(`rollback()`) al finalizar, sobre el mismo PostgreSQL de `docker-compose.yml`
(no una base de datos física separada por test). `join_transaction_mode=
"create_savepoint"` hace que un `session.commit()` dentro del código bajo prueba
solo libere/reabra un SAVEPOINT en vez de terminar la transacción externa, para
que el rollback final siga revirtiendo todo lo escrito durante el test.
"""
import pytest
from sqlalchemy.orm import Session

from db.session import engine


@pytest.fixture()
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection, join_transaction_mode="create_savepoint")
    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()
