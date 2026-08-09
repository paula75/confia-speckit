"""Unit tests: schema Pydantic de "Datos de profesionales" (FR-BW-003).

Ver specs/001-gestion-integral-reservas/tasks.md T011.
"""
import pytest
from pydantic import ValidationError

from models.profesional import ProfesionalCreateInput


def test_rechaza_payload_sin_nombre():
    with pytest.raises(ValidationError):
        ProfesionalCreateInput()


def test_acepta_payload_valido():
    input_ = ProfesionalCreateInput(nombre="Ana Pérez")
    assert input_.nombre == "Ana Pérez"
