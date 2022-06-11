from asyncio.log import logger
from typing import List
from app.models.models_proyectos import Proyecto, RecursoProyecto

from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.schemas.schemas_proyectos import ProyectoCreate, ProyectoDelete, ProyectoUpdate


# ------------------------- GET FUNCTIONS ------------------------------------------
def get_proyectos(db: Session) -> List[Proyecto]:
    try:
        proyectos = db.query(Proyecto).all()
        for proyecto in proyectos:
            proyecto.recursos = get_legajos_recursos(proyecto.codigo, db)
        return proyectos
    except Exception as e:
        logger.error("Error al obtener los riesgos: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al obtener los proyectos")

def get_proyecto(codigo: int, db: Session) -> Proyecto :
    proyecto = db.query(Proyecto).filter(Proyecto.codigo == codigo).first()
    if not proyecto :
        raise HTTPException(status_code=404, detail="El proyecto no existe")
        
    proyecto.recursos = get_legajos_recursos(proyecto.codigo, db)
    return proyecto

def get_proyecto_by_nombre(nombre: str, db: Session) -> Proyecto :
    return db.query(Proyecto).filter(Proyecto.nombre == nombre).first()

def get_recursos_by_proyecto(codigo_proyecto: int, db: Session) -> List[RecursoProyecto] :
    return db.query(RecursoProyecto).filter(RecursoProyecto.codigo_proyecto == codigo_proyecto).all()

def get_legajos_recursos(codigo_proyecto: int, db: Session) -> List[int]:
    legajos = []
    recursos = get_recursos_by_proyecto(codigo_proyecto, db)
    for recurso in recursos:
        legajos.append(recurso.legajo_recurso)
    return legajos


# ------------------------- SAVE FUNCTIONS ------------------------------------------
def save_recursos(recursos: List[int], codigo_proyecto: int, db: Session) -> List[int]:
    legajos = []
    for legajo in recursos:
        db_recurso = RecursoProyecto(
            codigo_proyecto=codigo_proyecto,
            legajo_recurso=legajo
        )
        db.add(db_recurso)
        legajos.append(legajo)
    db.commit()
    return legajos

def save_proyecto(proyecto: ProyectoCreate, db: Session) -> Proyecto :
    db_proyecto = Proyecto(
        nombre=proyecto.nombre,
        tipo=proyecto.tipo,
        fecha_limite = proyecto.fecha_limite
    )
    try:
        db.add(db_proyecto)
        db.commit()
        db_proyecto.recursos = save_recursos(proyecto.recursos, db_proyecto.codigo, db)
        return db_proyecto
    except Exception as e:
        logger.error("Error al agregar el proyecto: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al agregar el proyecto")


# ------------------------- UPDATE FUNCTIONS ------------------------------------------
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
        proyecto_old.recursos = update_recursos(proyecto_new, db)
        return proyecto_old
    except Exception as e:
        logger.error("Error al actualizar el proyecto: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al actualizar el proyecto")

def update_recursos(proyecto_new: ProyectoUpdate, db: Session) :
    delete_recursos(proyecto_new.codigo, db)
    new_recursos = save_recursos(proyecto_new.recursos, proyecto_new.codigo, db)
    return new_recursos


# ------------------------- DELETE FUNCTIONS ------------------------------------------
def delete_proyecto(codigo_proyecto: int, db: Session):
    try:
        delete_recursos(codigo_proyecto, db)
        proyecto = db.query(Proyecto).filter(Proyecto.codigo == codigo_proyecto).first()
        db.delete(proyecto)
        db.commit()
        return {"transaction": "ok"}
    except Exception as e:
        db.rollback()
        logger.error("Error al eliminar el proyecto: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al eliminar el proyecto")

def delete_recursos(codigo_proyecto: int, db: Session) -> None :
    try:
        recursos = db.query(RecursoProyecto).filter(RecursoProyecto.codigo_proyecto == codigo_proyecto).all()
        for recurso in recursos:
            db.delete(recurso)
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error("Error al eliminar los recursos del proyecto: " + str(e))
        raise HTTPException(status_code=500, detail="Problemas al eliminar los recursos del proyecto")