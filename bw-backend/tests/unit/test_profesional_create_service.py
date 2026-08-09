"""Unit tests: `ProfesionalService.crear()` — autorización + persistencia (FR-BW-005).

Ver specs/001-gestion-integral-reservas/tasks.md T012.
"""
import pytest

from models.profesional import ProfesionalCreateInput, ProfesionalORM
from services.auth import RolNoAutorizadoError
from services.profesional_service import ProfesionalService

ROL_AUTORIZADO = "Administrador de la operación"


def test_crear_persiste_para_rol_autorizado(db_session):
    service = ProfesionalService(db_session)
    input_ = ProfesionalCreateInput(nombre="Ana Pérez")

    profesional = service.crear(input_, rol=ROL_AUTORIZADO)

    assert profesional.nombre == "Ana Pérez"
    persistido = (
        db_session.query(ProfesionalORM).filter_by(id=profesional.id).one()
    )
    assert persistido.nombre == "Ana Pérez"


def test_crear_rechaza_rol_no_autorizado(db_session):
    service = ProfesionalService(db_session)
    input_ = ProfesionalCreateInput(nombre="Ana Pérez")

    with pytest.raises(RolNoAutorizadoError):
        service.crear(input_, rol="Coordinador de agenda")

    assert db_session.query(ProfesionalORM).count() == 0
