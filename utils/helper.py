from pydantic import BaseModel
from typing import Optional
from logger_config import logger

class SoldierCreate(BaseModel):
    
    full_name: str
    personal_number: str
    rank: str
    role: str
    unit: str
    status: str

class SoldierUpdate(BaseModel):
    full_name: Optional[str] = None
    personal_number: Optional[str] = None
    rank: Optional[str] = None
    role: Optional[str] = None
    unit: Optional[str] = None
    status: Optional[str] = None

class SoldierProfile(SoldierCreate):
    id: int
         
    
def get_soldier_by_id(soldiers: list, soldier_id: int):
    for soldier in soldiers:
            if soldier.get('id') == soldier_id:
                logger.info('ID was found.')
                return soldier
    return None