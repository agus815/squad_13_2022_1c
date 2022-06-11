from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine

from .routes import proyecto_routes
from .routes import riesgos_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(proyecto_routes.router, prefix="/proyectos", tags=["proyectos"])
app.include_router(riesgos_routes.router, prefix="/riesgos", tags=["riesgos"])