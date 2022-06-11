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
    proyectos = get_proyectos(db)
    return proyectos

@router.get("/{codigo}", response_model=Proyecto)
def read_proyecto(codigo: int, db: Session = Depends(get_db)):
    proyecto = get_proyecto(codigo, db)
    return proyecto
