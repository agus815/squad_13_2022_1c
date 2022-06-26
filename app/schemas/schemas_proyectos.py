from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field
from .schemas_tareas import Tarea


class ProyectoBase(BaseModel):
    nombre: Optional[str] = Field('', title="Nombre del proyecto")
    tipo: Optional[str] = Field('', title="Tipo del proyecto. Puede ser implementación o desarrollo")
    estado: Optional[str] = Field('Creado', title='Estado del proyecto (creado, en desarrollo, bloqueado o finalizado)')
    fecha_limite: Optional[date] = Field(date.today(), title="Fecha límite para completar el proyecto")


class ProyectoDelete(BaseModel):
    codigo: int = Field(..., title="Codigo del proyecto en la DB")


class ProyectoUpdate(ProyectoBase):
    codigo: int = Field(..., title="Codigo del proyecto en la DB")


class ProyectoCreate(ProyectoBase):
    nombre: str = Field(..., title="Nombre del proyecto")
    tipo: str = Field(..., title="Tipo del proyecto. Puede ser implementación o desarrollo")
    estado: str = Field(..., title="Estado del proyecto (creado, en desarrollo, bloqueado o finalizado)")
    fecha_limite: date = Field(..., title="Fecha límite para completar el proyecto")


class Proyecto(ProyectoBase):
    tareas: Optional[List[Tarea]] = Field([], title="Tareas asignadas al proyecto")
    codigo: int = Field(..., title="Codigo del proyecto en la DB")

    class Config:
        orm_mode = True
