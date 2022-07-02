from fastapi import APIRouter, Depends

from ..database import SessionLocal

from ..cruds.crud_tareas import *

from ..schemas.schemas_tareas import *

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[Tarea])
def read_tareas(db: Session = Depends(get_db)):
    return get_tareas(db)

@router.get("/{codigo}", response_model=Tarea)
def read_tarea(codigo: int, db: Session = Depends(get_db)):
    tarea = get_tarea(codigo, db)
    if not tarea:
        raise HTTPException(status_code=404, detail="La tarea no existe")
    return tarea


@router.get("/proyecto/{codigo_proyecto}", response_model=List[Tarea])
def read_tareas_by_proyecto(codigo_proyecto: int, db: Session = Depends(get_db)):
    return get_tareas_from_proyecto(codigo_proyecto, db)


@router.post("/create", response_model=Tarea)
def create_tarea(tarea: TareaCreate, db: Session = Depends(get_db)):
    return save_tarea(tarea, db)


@router.post("/update", response_model=Tarea)
def update_tarea_api(tarea: TareaUpdate, db: Session = Depends(get_db)):
    return update_tarea(tarea, db)


@router.post("/delete")
def remove_tarea(tarea: TareaDelete, db: Session = Depends(get_db)):
    return delete_tarea(tarea.codigo, db)
