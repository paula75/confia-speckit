"""Entrypoint for bw-backend (FastAPI application).

Bundle Backend/Frontend Web (BW), solo backend — ver specs/001-gestion-integral-reservas/plan.md.
"""
from fastapi import FastAPI

from api.profesionales import router as profesionales_router

app = FastAPI(
    title="bw-backend",
    description="Backend administrativo del bundle Backend/Frontend Web — Gestión de profesionales",
)

app.include_router(profesionales_router)
