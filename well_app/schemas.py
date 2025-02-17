from pydantic import BaseModel, ConfigDict
from datetime import datetime

class WellBase(BaseModel):
    id_well: int
    id_tag: int
    tag_val: str
    date_time: datetime

    model_config = ConfigDict(from_attributes=True)

class WellCreate(BaseModel):
    id_well: int
    id_tag: int
    tag_val: str
    date_time: datetime

    model_config = ConfigDict(from_attributes=True)

class Well(WellBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
