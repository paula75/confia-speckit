"""Control de autorización para las acciones administrativas restringidas de BW.

Aclarado (Clarifications, Sesión 2026-08-05 y 2026-08-08): únicamente el rol
"Administrador de la operación" (actor organizacional "Administrador del centro")
puede ejecutar crear/modificar profesional (FR-BW-005). `spec.md` no declara el
mecanismo de autenticación en sí (ver quickstart.md §Prerrequisitos) — esta
función solo valida un rol ya resuelto, no lo obtiene.
"""

ROL_AUTORIZADO = "Administrador de la operación"


class RolNoAutorizadoError(PermissionError):
    """El rol del solicitante no está autorizado para esta acción administrativa."""


def requerir_administrador_operacion(rol: str) -> None:
    """Lanza RolNoAutorizadoError si `rol` no es "Administrador de la operación"."""
    if rol != ROL_AUTORIZADO:
        raise RolNoAutorizadoError(
            f"El rol '{rol}' no está autorizado para esta acción; "
            f"se requiere '{ROL_AUTORIZADO}'."
        )
