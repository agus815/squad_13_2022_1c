from asyncio.log import logger
from typing import List
from app.models.models_tareas import Tarea
from app.models.models_proyectos import Proyecto

from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.schemas.schemas_tareas import TareaCreate, TareaUpdate


# ------------------------- GET FUNCTIONS ------------------------------------------
def get_tareas(db: Session) -> List[Tarea]:
    try:
        tareas = db.query(Tarea).all()
        return tareas
    except Exception:
        raise HTTPException(status_code=500, detail="Problemas al obtener las tareas")


def get_tareas_from_proyecto(codigo_proyecto: int, db: Session) -> List[Tarea]:
    try:
        tareas = db.query(Tarea).filter(Tarea.codigo_proyecto == codigo_proyecto).all()
        return tareas
    except Exception:
        raise HTTPException(status_code=500, detail="Problemas al obtener las tareas")


def get_tarea(codigo: int, db: Session) -> Tarea:
    tarea = db.query(Tarea).filter(Tarea.codigo == codigo).first()
    return tarea


# ------------------------- SAVE FUNCTIONS ------------------------------------------

def save_tarea(tarea: TareaCreate, db: Session) -> Tarea:
    proyecto = db.query(Proyecto).filter(Proyecto.codigo == tarea.codigo_proyecto).first()
    if not proyecto:
        raise HTTPException(status_code=400, detail="El proyecto no existe")
    db_tarea = Tarea(**tarea.dict())
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
        if tarea_new.nombre != None: tarea_old.nombre = tarea_new.nombre
        if tarea_new.descripcion != None: tarea_old.descripcion = tarea_new.descripcion
        if tarea_new.estado != None: tarea_old.estado =  tarea_new.estado
        if tarea_new.duracion != None: tarea_old.duracion = tarea_new.duracion
        if tarea_new.prioridad != None: tarea_old.prioridad = tarea_new.prioridad
        if tarea_new.fecha_inicio != None: tarea_old.fecha_inicio = tarea_new.fecha_inicio
        if tarea_new.fecha_fin != None: tarea_old.fecha_fin = tarea_new.fecha_fin
        if tarea_new.recurso != None: tarea_old.recurso = tarea_new.recurso
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