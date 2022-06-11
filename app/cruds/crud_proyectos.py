from asyncio.log import logger
from typing import List
from app.models.models_proyectos import Proyecto

from sqlalchemy.orm import Session

from fastapi import HTTPException

def get_proyectos(db: Session) -> List[Proyecto]:
    try:
        return db.query(Proyecto).all()
    except Exception as e:
        logger.error("Error al obtener los riesgos: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al obtener los proyectos")

def get_proyecto(codigo: int, db: Session) -> Proyecto :
    proyecto = db.query(Proyecto).filter(Proyecto.codigo == codigo).first()
    if not proyecto :
        raise HTTPException(status_code=404, detail="El proyecto no existe")

    return proyecto