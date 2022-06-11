from pydantic import BaseModel, Field

class RiesgoBase(BaseModel) :
    descripcion: str = Field(..., title="Descripcion del riesgo")
    probabilidad: float = Field(0.00, title="Probabilidad de que el riesgo ocurra")
    impacto: float = Field(0.00, title="Impacto que tiene el riesgo en caso de ocurrir")
    exposicion: float = Field(0.00, title="")

class RiesgoDelete(BaseModel) : 
    codigo: int = Field(..., title="Codigo del riesgo en la DB")

class RiesgoUpdate(RiesgoBase) :
    codigo: int = Field(..., title="Codigo del riesgo en la DB")

class RiesgoCreate(RiesgoBase):
    pass

class Riesgo(RiesgoBase):
    codigo: int = Field(..., title="Codigo del riesgo en la DB")
    class Config:
        orm_mode = True
