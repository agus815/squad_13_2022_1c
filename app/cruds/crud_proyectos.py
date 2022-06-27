from asyncio.log import logger
from typing import List
from app.models.models_proyectos import Proyecto
from app.models.models_tareas import Tarea

from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.schemas.schemas_proyectos import ProyectoCreate, ProyectoUpdate


# ------------------------- GET FUNCTIONS ------------------------------------------
def get_proyectos(db: Session) -> List[Proyecto]:
    try:
        proyectos = db.query(Proyecto).all()
        return proyectos
    except Exception as e:
        logger.error("Error al obtener los proyectos: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al obtener los proyectos")


def get_proyecto(codigo: int, db: Session) -> Proyecto:
    proyecto = db.query(Proyecto).filter(Proyecto.codigo == codigo).first()
    if not proyecto:
        raise HTTPException(status_code=404, detail="El proyecto no existe")
    return proyecto


def get_proyecto_by_nombre(nombre: str, db: Session) -> Proyecto:
    return db.query(Proyecto).filter(Proyecto.nombre == nombre).first()


# ------------------------- SAVE FUNCTIONS ------------------------------------------
def save_proyecto(proyecto: ProyectoCreate, db: Session) -> Proyecto:
    db_proyecto = Proyecto(
        nombre=proyecto.nombre,
        tipo=proyecto.tipo,
        estado=proyecto.estado,
        fecha_limite=proyecto.fecha_limite,
    )
    try:
        db.add(db_proyecto)
        db.commit()
        db_proyecto.tareas = save_tareas(proyecto.tareas, db)
        db.refresh(db_proyecto)
        return db_proyecto
    except Exception as e:
        logger.error("Error al agregar el proyecto: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al agregar el proyecto")


def save_tareas(tareas: List[Tarea], db: Session) -> List[Tarea]:
    t = []
    for tarea in tareas:
        db.add(tarea)
    db.commit()
    return t


# ------------------------- UPDATE FUNCTIONS ------------------------------------------
def update_proyecto(proyecto_new: ProyectoUpdate, db: Session) -> Proyecto:
    proyecto_old = get_proyecto(proyecto_new.codigo, db)
    if not proyecto_old:
        raise HTTPException(status_code=404, detail="El proyecto no existe")

    proyecto_db = get_proyecto_by_nombre(proyecto_new.nombre, db)
    if proyecto_db and proyecto_db.codigo != proyecto_new.codigo:
        raise HTTPException(status_code=400, detail="El nombre del proyecto ya existe")

    try:
        if proyecto_new.nombre: proyecto_old.nombre = proyecto_new.nombre
        if proyecto_new.tipo: proyecto_old.tipo = proyecto_new.tipo
        if proyecto_new.estado: proyecto_old.estado = proyecto_new.estado
        if proyecto_new.fecha_limite: proyecto_old.fecha_limite = proyecto_new.fecha_limite
        db.commit()
        db.refresh(proyecto_old)
        return proyecto_old
    except Exception as e:
        logger.error("Error al actualizar el proyecto: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al actualizar el proyecto")


# ------------------------- DELETE FUNCTIONS ------------------------------------------
def delete_proyecto(codigo_proyecto: int, db: Session):
    try:
        proyecto = db.query(Proyecto).filter(Proyecto.codigo == codigo_proyecto).first()
        db.delete(proyecto)
        db.commit()
        db.refresh
        return {"transaction": "ok"}
    except Exception as e:
        db.rollback()
        logger.error("Error al eliminar el proyecto: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al eliminar el proyecto")
