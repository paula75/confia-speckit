"""Unit tests: `ProfesionalService.modificar()` — autorización + persistencia (FR-BW-005).

Ver specs/001-gestion-integral-reservas/tasks.md T020.
"""
import pytest

from models.profesional import ProfesionalCreateInput, ProfesionalORM
from services.auth import RolNoAutorizadoError
from services.profesional_service import ProfesionalService

ROL_AUTORIZADO = "Administrador de la operación"


def test_modificar_persiste_para_rol_autorizado(db_session):
    existente = ProfesionalORM(nombre="Nombre Original", especialidades=[])
    db_session.add(existente)
    db_session.commit()

    service = ProfesionalService(db_session)
    actualizado = service.modificar(
        existente.id, ProfesionalCreateInput(nombre="Nombre Actualizado"), rol=ROL_AUTORIZADO
    )

    assert actualizado.nombre == "Nombre Actualizado"
    db_session.refresh(existente)
    assert existente.nombre == "Nombre Actualizado"


def test_modificar_rechaza_rol_no_autorizado(db_session):
    existente = ProfesionalORM(nombre="Nombre Original", especialidades=[])
    db_session.add(existente)
    db_session.commit()

    service = ProfesionalService(db_session)
    with pytest.raises(RolNoAutorizadoError):
        service.modificar(
            existente.id, ProfesionalCreateInput(nombre="Otro"), rol="Coordinador de agenda"
        )

    db_session.refresh(existente)
    assert existente.nombre == "Nombre Original"
