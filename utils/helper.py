from pydantic import BaseModel, ValidationError
from logger_config import logger

class SoldierProfile(BaseModel):
    
    id: int
    full_name: str
    personal_number: str
    rank: str
    role: str
    unit: str
    status: str

        
def soldier_data_validation(data: dict):
    try:
        SoldierProfile.model_validate(data)
        return data
    except ValidationError as e:
        logger.warning(f'Soldier data validation stopped, error: {e}.')
        
        for error in e.errors():
            field_name = str(error['loc'][0]) if error['loc'] else "global"
            error_type = error['type']
            error_msg = error['msg']

            if error_type == 'missing':
                logger.error(f'missing: {field_name} in data.')
                return (error_type, field_name)
            else:
                logger.error(f'Invalid {field_name} in data, error: {error_msg}')
                return (error_type, field_name)
         
        
def get_soldier_by_id(soldiers: list, soldier_id: int):
    for soldier in soldiers:
            if soldier.get('id') == soldier_id:
                return soldier
    return None