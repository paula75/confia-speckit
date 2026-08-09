"""ProfesionalService: lógica de negocio de "Gestión de profesionales".

Ver specs/001-gestion-integral-reservas/data-model.md y contracts/.
"""
import uuid

from sqlalchemy.orm import Session

from models.profesional import Profesional, ProfesionalCreateInput, ProfesionalORM
from services.auth import requerir_administrador_operacion


class ProfesionalService:
    def __init__(self, db: Session):
        self.db = db

    def crear(self, input_: ProfesionalCreateInput, rol: str) -> Profesional:
        """Crea un profesional nuevo (FR-BW-005), restringido al rol autorizado."""
        requerir_administrador_operacion(rol)

        orm = ProfesionalORM(id=uuid.uuid4(), nombre=input_.nombre, especialidades=[])
        self.db.add(orm)
        self.db.commit()
        self.db.refresh(orm)
        return Profesional.model_validate(orm)

    def listar(self) -> list[Profesional]:
        """Lectura directa a PostgreSQL (FR-BW-011); respalda "Profesionales Query
        API" (FR-BW-031, servida por BW — ver contracts/bw-shared-internal-api.md
        §Parte 1)."""
        registros = self.db.query(ProfesionalORM).order_by(ProfesionalORM.nombre).all()
        return [Profesional.model_validate(r) for r in registros]
