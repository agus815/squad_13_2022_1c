from asyncio.log import logger
from typing import List
from app.models.models_tareas import Tarea, RecursoTarea

from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.schemas.schemas_tareas import TareaCreate, TareaDelete, TareaUpdate


# ------------------------- GET FUNCTIONS ------------------------------------------
"""def get_tareas(db: Session) -> List[Tarea]:
    try:
        tareas = db.query(Tarea).all()
        return tareas
    except Exception:
        raise HTTPException(status_code=500, detail="Problemas al obtener las tareas")"""


def get_tareas_from_proyecto(codigo_proyecto: int, db: Session) -> List[Tarea]:
    try:
        tareas = db.query(Tarea).filter(Tarea.codigo_proyecto == codigo_proyecto).all()
        return tareas
    except Exception:
        raise HTTPException(status_code=500, detail="Problemas al obtener las tareas")


def get_tarea(codigo: int, db: Session) -> Tarea:
    tarea = db.query(Tarea).filter(Tarea.codigo == codigo).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="La tarea no existe")
    return tarea


def get_tarea_by_name(nombre: str, db: Session) -> Tarea:
    return db.query(Tarea).filter(Tarea.nombre == nombre).first()


# ------------------------- SAVE FUNCTIONS ------------------------------------------

def save_tarea(tarea: TareaCreate, db: Session) -> Tarea:
    db_tarea = Tarea(
        codigo_proyecto=tarea.codigo_proyecto,
        nombre=tarea.nombre,
        descripcion=tarea.descripcion,
        estado=tarea.estado,
        duracion=tarea.duracion,
        prioridad=tarea.prioridad,
        fecha_inicio=tarea.fecha_inicio,
        fecha_fin=tarea.fecha_fin
    )
    try:
        db.add(db_tarea)
        db.commit()
        return db_tarea
    except Exception as e:
        logger.error("Error al agregar la tarea: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al agregar la tarea")


# ------------------------- UPDATE FUNCTIONS ------------------------------------------
def update_tarea(tarea_new: TareaUpdate, db: Session) -> Tarea:
    tarea_old = get_tarea(tarea_new.codigo, db)
    if not tarea_old:
        raise HTTPException(status_code=404, detail="La tarea no existe")

    try:
        tarea_old.nombre = tarea_new.nombre
        tarea_old.descripcion = tarea_new.descripcion
        tarea_old.estado = tarea_new.estado
        tarea_old.duracion = tarea_new.duracion
        tarea_old.prioridad = tarea_new.prioridad
        tarea_old.fecha_inicio = tarea_new.fecha_inicio
        tarea_old.fecha_fin = tarea_new.fecha_fin
        db.commit()
        return tarea_old
    except Exception as e:
        logger.error("Error al actualizar la tarea: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al actualizar la tarea")


# ------------------------- DELETE FUNCTIONS ------------------------------------------
def delete_tarea(codigo_tarea: int, db: Session):
    try:
        tarea = db.query(Tarea).filter(Tarea.codigo == codigo_tarea).first()
        db.delete(tarea)
        db.commit()
        return {"transaction": "ok"}
    except Exception as e:
        db.rollback()
        logger.error("Error al eliminar la tarea: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al eliminar la tarea")
