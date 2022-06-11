from fastapi import APIRouter, Depends, HTTPException
from typing import List

from sqlalchemy.orm import Session

from ..database import SessionLocal

from ..cruds.crud_riesgos import *

from ..schemas.schemas_riesgos import *

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[Riesgo])
def read_riesgos(db: Session = Depends(get_db)):
    riesgos = get_riesgos(db)
    return riesgos

@router.get("/{codigo}", response_model=Riesgo)
def read_riesgo(codigo: int, db: Session = Depends(get_db)):
    riesgo = get_riesgo(codigo, db)
    return riesgo
