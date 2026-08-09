"""Router FastAPI para "Gestión de profesionales" (FR-BW-003, 005, 011, 025, 031, 037).

Los endpoints se agregan en las fases de historia de usuario correspondientes
(ver specs/001-gestion-integral-reservas/tasks.md).
"""
from fastapi import APIRouter

router = APIRouter(prefix="/profesionales", tags=["profesionales"])
