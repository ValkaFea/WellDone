from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session
from . import models, schemas

def add_val(db: Session, well: schemas.WellCreate):
    db_well = models.Well(
        id_well=well.id_well,
        id_tag=well.id_tag,
        tag_val=well.tag_val,
        date_time=well.date_time
    )
    try:
        db.add(db_well)
        db.commit()
        db.refresh(db_well)
        return db_well
    except IntegrityError:
        db.rollback()
        raise ValueError("Запись с такими id_well и id_tag уже существует")
    except SQLAlchemyError as e:
        db.rollback()
        raise ValueError(f"Ошибка базы данных: {str(e)}")

def get_all_val(db: Session):
    try:
        return db.query(models.Well).all()
    except SQLAlchemyError as e:
        raise ValueError(f"Ошибка при получении данных: {str(e)}")

def get_val_by_well(db: Session, id_well: int):
    try:
        measurements = db.query(models.Well).filter(models.Well.id_well == id_well).all()
        return measurements if measurements else None
    except SQLAlchemyError as e:
        raise ValueError(f"Ошибка при получении данных: {str(e)}")

def delete_well(db: Session, id_well: int) -> bool:
    try:
        well = db.query(models.Well).filter(models.Well.id_well == id_well).first()
        if well:
            db.delete(well)
            db.commit()
            return True
        return False
    except SQLAlchemyError as e:
        db.rollback()
        raise ValueError(f"Ошибка при удалении данных: {str(e)}")