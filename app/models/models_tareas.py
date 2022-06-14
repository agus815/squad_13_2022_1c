from sqlalchemy import Column, Integer, String, Date

from app.database import Base


class Tarea(Base):
    __tablename__ = 'tareas'
    codigo = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    codigo_proyecto = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50))
    descripcion = Column(String(50))
    estado = Column(String(50))
    duracion = Column(Integer)
    prioridad = Column(String(50))
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)


class RecursoTarea(Base):
    __tablename__ = 'tareas-recurso'
    codigo_tarea = Column(Integer, primary_key=True, nullable=False)
    legajo_recurso = Column(Integer, nullable=False)
