"""Router FastAPI para "Gestión de profesionales" (FR-BW-003, 005, 011, 025, 031, 037).

Nota de alcance — rol del solicitante: `spec.md` no declara el mecanismo de
autenticación (ver quickstart.md §Prerrequisitos); esta ejecución no lo inventa.
Los endpoints administrativos reciben el rol ya resuelto mediante el header
`X-Rol` (equivalente a lo que un gateway de autenticación inyectaría), solo
para poder ejercitar la autorización de FR-BW-005 que sí está en alcance.

Nota técnica — codificación del header: los headers HTTP se decodifican como
Latin-1 (RFC 7230), no UTF-8; el nombre del rol autorizado en `spec.md`
("Administrador de la operación") contiene una tilde que se corrompe si se
envía tal cual en un header. Por eso el header usa un código ASCII-safe
(`administrador-operacion`) que se traduce aquí al valor interno exacto de
`services/auth.ROL_AUTORIZADO` — el nombre del rol en `spec.md` no cambia, solo
su representación en tránsito HTTP.
"""
import uuid

from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from models.profesional import Profesional, ProfesionalCreateInput
from services.auth import ROL_AUTORIZADO, RolNoAutorizadoError
from services.profesional_service import ProfesionalService

router = APIRouter(prefix="/profesionales", tags=["profesionales"])

_CODIGO_HEADER_ADMIN_OPERACION = "administrador-operacion"


def _resolver_rol(x_rol: str) -> str:
    """Traduce el código ASCII-safe del header al rol interno cuando corresponde;
    cualquier otro valor se usa tal cual (no autorizado por definición)."""
    if x_rol == _CODIGO_HEADER_ADMIN_OPERACION:
        return ROL_AUTORIZADO
    return x_rol


@router.post("", response_model=Profesional, status_code=201)
def crear_profesional(
    input_: ProfesionalCreateInput,
    x_rol: str = Header(..., alias="X-Rol"),
    db: Session = Depends(get_db),
) -> Profesional:
    """FR-BW-005 "Crear/Modificar profesional" (variante crear)."""
    service = ProfesionalService(db)
    try:
        return service.crear(input_, rol=_resolver_rol(x_rol))
    except RolNoAutorizadoError as exc:
        raise HTTPException(status_code=403, detail=str(exc)) from exc


@router.get("/query", response_model=list[Profesional])
def profesionales_query_api(db: Session = Depends(get_db)) -> list[Profesional]:
    """FR-BW-031 "Profesionales Query API" — servida por BW, respaldada por su
    propio PostgreSQL (ver contracts/bw-shared-internal-api.md §Parte 1). Sin
    restricción de rol: es un contrato interno entre bundles, no una acción
    administrativa humana (distinto de FR-BW-005)."""
    return ProfesionalService(db).listar()


@router.get("", response_model=list[Profesional])
def listar_profesionales(db: Session = Depends(get_db)) -> list[Profesional]:
    """FR-BW-025 "Mostrar o notificar Ficha Profesionales" (listado administrativo)."""
    return ProfesionalService(db).listar()


@router.get("/{profesional_id}", response_model=Profesional)
def obtener_profesional(profesional_id: uuid.UUID, db: Session = Depends(get_db)) -> Profesional:
    """FR-BW-025 "Mostrar o notificar Ficha Profesionales" (ficha individual)."""
    for profesional in ProfesionalService(db).listar():
        if profesional.id == profesional_id:
            return profesional
    raise HTTPException(status_code=404, detail="Profesional no encontrado")
