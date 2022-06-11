from asyncio.log import logger
from typing import List
from app.models.models_proyectos import Proyecto

from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.schemas.schemas_proyectos import ProyectoCreate, ProyectoDelete, ProyectoUpdate

def get_proyectos(db: Session) -> List[Proyecto]:
    try:
        return db.query(Proyecto).all()
    except Exception as e:
        logger.error("Error al obtener los riesgos: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al obtener los proyectos")

def get_proyecto(codigo: int, db: Session) -> Proyecto :
    return db.query(Proyecto).filter(Proyecto.codigo == codigo).first()

def get_proyecto_by_nombre(nombre: str, db: Session) -> Proyecto :
    return db.query(Proyecto).filter(Proyecto.nombre == nombre).first()

def save_proyecto(proyecto: ProyectoCreate, db: Session) -> Proyecto :
    db_proyecto = Proyecto(
        nombre=proyecto.nombre,
        tipo=proyecto.tipo,
        fecha_limite = proyecto.fecha_limite
    )
    try:
        db.add(db_proyecto)
        db.commit()
        db.refresh(db_proyecto)
        return db_proyecto
    except Exception as e:
        logger.error("Error al agregar el proyecto: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al agregar el proyecto")

def update_proyecto(proyecto_new: ProyectoUpdate, db: Session) -> Proyecto:
    proyecto_old = get_proyecto(proyecto_new.codigo, db)
    if not proyecto_old :
        raise HTTPException(status_code=404, detail="El proyecto no existe")

    proyecto_db = get_proyecto_by_nombre(proyecto_new.nombre, db)
    if proyecto_db :
        raise HTTPException(status_code=400, detail="El nombre del proyecto ya existe")

    try:
        proyecto_old.nombre = proyecto_new.nombre
        proyecto_old.tipo = proyecto_new.tipo
        proyecto_old.fecha_limite = proyecto_new.fecha_limite
        db.commit()
        return proyecto_old
    except Exception as e:
        logger.error("Error al actualizar el proyecto: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al actualizar el proyecto")

def delete_proyecto(codigo_proyecto: int, db: Session):
    try:
        proyecto = db.query(Proyecto).filter(Proyecto.codigo == codigo_proyecto).first()
        db.delete(proyecto)
        db.commit()
        return {"transaction": "ok"}
    except Exception as e:
        db.rollback()
        logger.error("Error al eliminar el proyecto: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al eliminar el proyecto")