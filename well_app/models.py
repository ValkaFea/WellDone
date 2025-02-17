from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from .database import Base


class Well(Base):
    __tablename__ = 'well'
    id = Column(Integer, primary_key=True, index=True)
    id_well = Column(Integer, index=True)
    id_tag = Column(Integer, index=True)
    tag_val = Column(String, index=True)
    date_time = Column(DateTime, index=True)

    __table_args__ = (UniqueConstraint('id_well', 'id_tag', name='uix_id_well_id_tag'),)