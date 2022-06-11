from sqlalchemy import Column, Integer, Float, Text

from app.database import Base

class Riesgo(Base):
    __tablename__='riesgos'
    codigo = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    descripcion = Column(Text)
    probabilidad = Column(Float)
    impacto = Column(Float)
    exposicion = Column(Float)