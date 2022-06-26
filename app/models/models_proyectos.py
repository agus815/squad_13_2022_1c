from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from app.database import Base


class Proyecto(Base):
    __tablename__ = 'proyectos'
    codigo = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(50))
    tipo = Column(String(50))
    estado = Column(String(50))
    fecha_limite = Column(Date)
    tareas = relationship("Tarea", cascade="all,delete,delete-orphan")
