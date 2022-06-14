from datetime import date
from typing import Optional
from pydantic import BaseModel, Field


class TareaRecurso(BaseModel):
    codigo_tarea: int = Field(..., title="Código de la tarea al que el recurso fue asignado")
    legajo_recurso: int = Field(..., title="Número de legajo del recurso asigando")


class TareaBase(BaseModel):
    codigo_proyecto: int = Field(..., title="Código del proyecto al cual la tarea pertenece")
    nombre: str = Field(..., title="Nombre de la tarea")
    descripcion: str = Field(..., title="Descripcion de la tarea")
    estado: str = Field(..., title="Estado de la tarea")
    duracion: int = Field(..., title="Duracion en horas de la tarea")
    prioridad: str = Field(..., title="Prioridad de la tarea. Puede ser alta, media o baja")
    fecha_inicio: date = Field(date.today(), title="Fecha donde se inicia la tarea")
    fecha_fin: date = Field(date.today(), title="Fecha estimada para finalizar la tarea")
    recurso: Optional[int] = Field(..., title="Número de legajo del recurso asignado")


class TareaDelete(BaseModel):
    codigo: int = Field(..., title="Codigo de la tarea en la DB")


class TareaUpdate(TareaBase):
    codigo: int = Field(..., title="Codigo de la tarea en la DB")


class TareaCreate(TareaBase):
    pass


class Tarea(TareaBase):
    codigo: int = Field(..., title="Codigo de la tarea en la DB")

    class Config:
        orm_mode = True
