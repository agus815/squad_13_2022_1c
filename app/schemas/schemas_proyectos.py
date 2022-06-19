from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field
from .schemas_tareas import Tarea


class ProyectoRecurso(BaseModel):
    codigo_proyecto: int = Field(..., title="Código del proyecto al que el recurso fue asignado")
    legajo_recurso: int = Field(..., title="Número de legajo del recurso asigando")


class ProyectoBase(BaseModel):
    nombre: Optional[str] = Field('', title="Nombre del proyecto")
    tipo: Optional[str] = Field('', title="Tipo del proyecto. Puede ser implementación o desarrollo")
    fecha_limite: Optional[date] = Field(date.today(), title="Fecha límite para completar el proyecto")
    recursos: Optional[List[int]] = Field([], title="Números de legajo de los recursos asignados")


class ProyectoDelete(BaseModel):
    codigo: int = Field(..., title="Codigo del proyecto en la DB")


class ProyectoUpdate(ProyectoBase):
    codigo: int = Field(..., title="Codigo del proyecto en la DB")


class ProyectoCreate(ProyectoBase):
    nombre: str = Field(..., title="Nombre del proyecto")
    tipo: str = Field(..., title="Tipo del proyecto. Puede ser implementación o desarrollo")
    fecha_limite: date = Field(..., title="Fecha límite para completar el proyecto")


class Proyecto(ProyectoBase):
    tareas: Optional[List[Tarea]] = Field([], title="Tareas asignadas al proyecto")
    codigo: int = Field(..., title="Codigo del proyecto en la DB")

    class Config:
        orm_mode = True