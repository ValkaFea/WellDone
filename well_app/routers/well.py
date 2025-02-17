from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..crud import get_all_val, get_val_by_well, delete_well
from .. database import SessionLocal, engine, Base
from ..schemas import Well

Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/wells/", response_model=schemas.WellCreate)
def create_well(well: schemas.WellCreate, db: Session = Depends(get_db)):
    return crud.add_val(db=db, well=well)


@router.get("/wells/", response_model=list[Well])
def read_wells(db: Session = Depends(get_db)):
    return get_all_val(db)

@router.get("/wells/{id_well}/measurements", response_model=list[Well])
def read_measurements(id_well: int, db: Session = Depends(get_db)):
    measurements = get_val_by_well(db, id_well)
    if measurements is None:
        raise HTTPException(status_code=404, detail="Скважина не найдена")
    return measurements

@router.delete("/wells/{id_well}")
def remove_well(id_well: int, db: Session = Depends(get_db)):
    if not delete_well(db, id_well):
        raise HTTPException(status_code=404, detail="Скважина не найдена")
    return {"detail": "Скважина успешно удалена"}