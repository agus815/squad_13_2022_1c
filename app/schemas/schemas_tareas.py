from datetime import date
from typing import Optional
from pydantic import BaseModel, Field

class TareaBase(BaseModel):
    codigo_proyecto: int = Field(..., title="Código del proyecto al cual la tarea pertenece")
    nombre: str = Field(..., title="Nombre de la tarea")
    descripcion: str = Field(..., title="Descripcion de la tarea")
    estado: str = Field(..., title="Estado de la tarea")
    duracion: int = Field(..., title="Duracion en horas de la tarea")
    prioridad: str = Field(..., title="Prioridad de la tarea. Puede ser alta, media o baja")
    fecha_inicio: date = Field(date.today(), title="Fecha donde se inicia la tarea")
    fecha_fin: date = Field(date.today(), title="Fecha estimada para finalizar la tarea")
    recurso: Optional[int] = Field(None, title="Número de legajo del recurso asignado")


class TareaDelete(BaseModel):
    codigo: int = Field(..., title="Codigo de la tarea en la DB")


class TareaUpdate(TareaBase):
    codigo: int = Field(..., title="Codigo de la tarea en la DB")
    nombre: Optional[str] = Field(None, title="Nombre de la tarea")
    descripcion: Optional[str] = Field(None, title="Descripcion de la tarea")
    estado: Optional[str] = Field(None, title="Estado de la tarea")
    duracion: Optional[int] = Field(None, title="Duracion en horas de la tarea")
    prioridad: Optional[str] = Field(None, title="Prioridad de la tarea. Puede ser alta, media o baja")
    fecha_inicio: Optional[date] = Field(date.today(), title="Fecha donde se inicia la tarea")
    fecha_fin: Optional[date] = Field(date.today(), title="Fecha estimada para finalizar la tarea")

class TareaUpdateFromProyecto(TareaBase):
    codigo: Optional[int] = Field(None, title="Codigo de la tarea en la DB")
    nombre: Optional[str] = Field(None, title="Nombre de la tarea")
    descripcion: Optional[str] = Field(None, title="Descripcion de la tarea")
    estado: Optional[str] = Field(None, title="Estado de la tarea")
    duracion: Optional[int] = Field(None, title="Duracion en horas de la tarea")
    prioridad: Optional[str] = Field(None, title="Prioridad de la tarea. Puede ser alta, media o baja")
    fecha_inicio: Optional[date] = Field(date.today(), title="Fecha donde se inicia la tarea")
    fecha_fin: Optional[date] = Field(date.today(), title="Fecha estimada para finalizar la tarea")

class TareaCreate(TareaBase):
    codigo_proyecto: Optional[int] = Field(None, title="Código del proyecto al cual la tarea pertenece")

class Tarea(TareaBase):
    codigo: int = Field(..., title="Codigo de la tarea en la DB")

    class Config:
        orm_mode = True
