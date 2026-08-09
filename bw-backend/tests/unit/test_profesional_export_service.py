"""Unit tests: `ProfesionalService.exportar()` (FR-BW-037).

Ver specs/001-gestion-integral-reservas/tasks.md T023.
"""
from models.profesional import ProfesionalORM
from services.profesional_service import ProfesionalService


def test_exportar_serializa_lista_completa(db_session):
    db_session.add_all(
        [
            ProfesionalORM(nombre="Ana Pérez", especialidades=["corte"]),
            ProfesionalORM(nombre="Luis Gómez", especialidades=[]),
        ]
    )
    db_session.commit()

    service = ProfesionalService(db_session)
    resultado = service.exportar()

    nombres = {p.nombre for p in resultado}
    assert nombres == {"Ana Pérez", "Luis Gómez"}


def test_exportar_vacio_cuando_no_hay_profesionales(db_session):
    service = ProfesionalService(db_session)
    assert service.exportar() == []
