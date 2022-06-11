from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field

class ProyectoRecurso(BaseModel) :
    codigo_proyecto: int = Field(..., title="Código del proyecto al que el recurso fue asignado")
    legajo_recurso: int = Field(..., title="Número de legajo del recurso asigando")

class ProyectoBase(BaseModel) :
    nombre: str = Field(..., title="Nombre del proyecto")
    tipo: str = Field(..., title="Tipo del proyecto. Puede ser implementación o desarrollo")
    fecha_limite: date = Field(date.today(), title="Fecha límite para completar el proyecto")
    recursos: Optional[List[int]] = Field([], title="Números de legajo de los recursos asignados")

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