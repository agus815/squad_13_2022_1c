from asyncio.log import logger
from typing import List
from app.models.models_riesgos import Riesgo

from sqlalchemy.orm import Session

from fastapi import HTTPException

def get_riesgos(db: Session) -> List[Riesgo]:
    try:
        return db.query(Riesgo).all()
    except Exception as e:
        logger.error("Error al obtener los riesgos: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al obtener los riesgos")

def get_riesgo(codigo: int, db: Session) -> Riesgo :
    riesgo = db.query(Riesgo).filter(Riesgo.codigo == codigo).first()
    if not riesgo :
        raise HTTPException(status_code=404, detail="El riesgo no existe")

    return riesgo
    