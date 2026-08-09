"""Unit tests: `ProfesionalService.listar()` (FR-BW-011, FR-BW-031).

Ver specs/001-gestion-integral-reservas/tasks.md T016.
"""
from models.profesional import ProfesionalORM
from services.profesional_service import ProfesionalService


def test_listar_devuelve_todos_los_profesionales(db_session):
    db_session.add_all(
        [
            ProfesionalORM(nombre="Ana Pérez", especialidades=["corte"]),
            ProfesionalORM(nombre="Luis Gómez", especialidades=[]),
        ]
    )
    db_session.commit()

    service = ProfesionalService(db_session)
    resultado = service.listar()

    nombres = {p.nombre for p in resultado}
    assert nombres == {"Ana Pérez", "Luis Gómez"}


def test_listar_vacio_cuando_no_hay_profesionales(db_session):
    service = ProfesionalService(db_session)
    assert service.listar() == []
