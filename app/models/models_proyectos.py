from sqlalchemy import Column, Integer, String, Date

from app.database import Base


class Proyecto(Base):
    __tablename__ = 'proyectos'
    codigo = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(50))
    tipo = Column(String(50))
    fecha_limite = Column(Date)


class RecursoProyecto(Base):
    __tablename__ = 'proyectos_recursos'
    codigo_proyecto = Column(Integer, primary_key=True, nullable=False)
    legajo_recurso = Column(Integer, nullable=False)
