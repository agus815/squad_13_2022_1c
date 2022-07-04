from asyncio.log import logger
from typing import List
from app.models.models_proyectos import Proyecto
from app.models.models_tareas import Tarea
from app.cruds.crud_tareas import get_tarea, update_tarea, save_tarea, get_tareas_from_proyecto, delete_tarea

from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.schemas.schemas_proyectos import ProyectoCreate, ProyectoUpdate
from app.schemas.schemas_tareas import TareaCreate, TareaUpdateFromProyecto, TareaUpdate


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
        db.refresh(db_proyecto)
        tareas=list(tarea_generator(proyecto, db_proyecto.codigo))
        for tarea in tareas:
            save_tarea(tarea, db)
        return db_proyecto
    except Exception as e:
        logger.error("Error al agregar el proyecto: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al agregar el proyecto")


def tarea_generator(proyecto: ProyectoCreate, codigo_proyecto: int):
    for tarea in proyecto.tareas:
        new_tarea = TareaCreate(**tarea.dict())
        new_tarea.codigo_proyecto = codigo_proyecto
        yield new_tarea


# ------------------------- UPDATE FUNCTIONS ------------------------------------------
def update_proyecto(proyecto_new: ProyectoUpdate, db: Session) -> Proyecto:
    proyecto_old = get_proyecto(proyecto_new.codigo, db)
    if not proyecto_old:
        raise HTTPException(status_code=404, detail="El proyecto no existe")

    proyecto_db = get_proyecto_by_nombre(proyecto_new.nombre, db)
    if proyecto_db and proyecto_db.codigo != proyecto_new.codigo:
        raise HTTPException(status_code=400, detail="El nombre del proyecto ya existe")

    try:
        if proyecto_new.nombre != None: proyecto_old.nombre = proyecto_new.nombre
        if proyecto_new.tipo != None: proyecto_old.tipo = proyecto_new.tipo
        if proyecto_new.estado != None: proyecto_old.estado = proyecto_new.estado
        if proyecto_new.fecha_limite != None: proyecto_old.fecha_limite = proyecto_new.fecha_limite
        old_tareas = get_tareas_from_proyecto(proyecto_new.codigo, db)
        new_tareas = []
        for tarea in proyecto_new.tareas :
            tarea_db = get_tarea(tarea.codigo, db)
            if tarea_db :
                if tarea_db in old_tareas:
                    tarea_new = TareaUpdate(**tarea.dict())
                    tarea_updated = update_tarea(tarea_new, db)
                    new_tareas.append(tarea_updated.codigo)
            else:
                tarea_create = TareaCreate(
                    codigo_proyecto=tarea.codigo_proyecto,
                    nombre=tarea.nombre,
                    descripcion=tarea.descripcion,
                    estado=tarea.estado,
                    duracion=tarea.duracion,
                    prioridad=tarea.prioridad,
                    fecha_inicio=tarea.fecha_inicio,
                    fecha_fin=tarea.fecha_fin,
                    recurso=tarea.recurso
                )
                tarea_saved = save_tarea(tarea_create, db)
                new_tareas.append(tarea_saved.codigo)
        for tarea in old_tareas :
            if tarea.codigo not in new_tareas:
                delete_tarea(tarea.codigo, db)
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
