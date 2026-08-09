"""Profesional: entidad propia de BW, tabla `profesionales` en PostgreSQL.

Ver specs/001-gestion-integral-reservas/data-model.md §Profesionales y especialidades.
"""
import uuid

from pydantic import BaseModel
from sqlalchemy import ARRAY, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class ProfesionalORM(Base):
    """Tabla `profesionales` — FR-BW-003, FR-BW-005, FR-BW-011, FR-BW-025, FR-BW-031, FR-BW-037."""

    __tablename__ = "profesionales"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    especialidades: Mapped[list[str]] = mapped_column(
        ARRAY(String), nullable=False, default=list
    )


class Profesional(BaseModel):
    """Schema Pydantic de salida — misma forma que ProfesionalORM."""

    id: uuid.UUID
    nombre: str
    especialidades: list[str]

    model_config = {"from_attributes": True}
