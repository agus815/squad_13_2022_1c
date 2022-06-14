from fastapi import APIRouter, Depends, HTTPException
from typing import List

from sqlalchemy.orm import Session

from ..database import SessionLocal

from ..cruds.crud_proyectos import *

from ..schemas.schemas_proyectos import *

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[Proyecto])
def read_proyectos(db: Session = Depends(get_db)):
    return get_proyectos(db)


@router.get("/{codigo}", response_model=Proyecto)
def read_proyecto(codigo: int, db: Session = Depends(get_db)):
    return get_proyecto(codigo, db)


@router.post("/create", response_model=Proyecto)
def create_proyecto(proyecto: ProyectoCreate, db: Session = Depends(get_db)):
    proyecto_db = get_proyecto_by_nombre(proyecto.nombre, db)
    if proyecto_db:
        raise HTTPException(status_code=400, detail="El proyecto ya estaba registrado")
    return save_proyecto(proyecto, db)


@router.post("/update", response_model=Proyecto)
def update_proyecto_api(proyecto: ProyectoUpdate, db: Session = Depends(get_db)):
    return update_proyecto(proyecto, db)


@router.post("/delete")
def remove_proyecto(proyecto: ProyectoDelete, db: Session = Depends(get_db)):
    return delete_proyecto(proyecto.codigo, db)
