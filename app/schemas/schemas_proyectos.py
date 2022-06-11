from datetime import date
from pydantic import BaseModel, Field

class ProyectoBase(BaseModel) :
    nombre: str = Field(..., title="Nombre del proyecto")
    tipo: str = Field(..., title="Tipo del proyecto. Puede ser implementación o desarrollo")
    fecha_limite: date = Field(date.today(), title="Impacto que tiene el riesgo en caso de ocurrir")

class ProyectoDelete(BaseModel) : 
    codigo: int = Field(..., title="Codigo del proyecto en la DB")

class ProyectoUpdate(ProyectoBase) :
    codigo: int = Field(..., title="Codigo del proyecto en la DB")

class ProyectoCreate(ProyectoBase):
    pass

class Proyecto(ProyectoBase):
    codigo: int = Field(..., title="Codigo del proyecto en la DB")
    class Config:
        orm_mode = True