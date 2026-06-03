from pydantic import BaseModel, ValidationError
from logger_config import logger

class SoldierCreate(BaseModel):
    
    full_name: str
    personal_number: str
    rank: str
    role: str
    unit: str
    status: str

class SoldierUpdate(BaseModel):
    full_name: str | None = None
    personal_number: str | None = None
    rank: str | None = None
    role: str | None = None
    unit: str | None = None
    status: str | None = None

class SoldierProfile(SoldierCreate):
    id: int
         
    
def get_soldier_by_id(soldiers: list, soldier_id: int):
    for soldier in soldiers:
            if soldier.get('id') == soldier_id:
                return soldier
    return None