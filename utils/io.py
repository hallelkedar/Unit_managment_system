import os
import json
from logger_config import logger
from utils.helper import get_soldier_by_id, soldier_data_validation

FILE_NAME = 'soldiers.json'

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        data = []
        json.dump(data, f, indent=2)


def read_json():
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def write_back_to_json(data, file):
    file.seek(0)
    json.dump(data, file, indent=2)
    file.truncate()

def get_all_soldiers():

    soldiers = read_json()
    logger.info('Open soldiers json file, Return dict')
    
    if len(soldiers) == 0:
        logger.warning('Soldiers list is empty.')
    
    return soldiers

def get_soldier(soldier_id: int):
        
    soldiers = read_json()
    return get_soldier_by_id(soldiers, soldier_id)
    
def create_soldier(data: dict):
    with open(FILE_NAME, 'r+', encoding='utf-8') as f:
        soldiers: list = json.load(f)
        next_id = max(soldier['id'] for soldier in soldiers) + 1 if soldiers else 1
        data['id'] = next_id
        validation = soldier_data_validation(data)
        if validation == data:
            soldiers.append(data)

            write_back_to_json(soldiers, f)
            return True, next_id
        return False, validation
        

def update_soldier(soldier_id: int, data: dict):
    with open(FILE_NAME, 'r+', encoding='utf-8') as f:
        
        soldiers = json.load(f)
        soldier:dict | None = get_soldier_by_id(soldiers, soldier_id)
        
        if not soldier:
            logger.error('ID was not found')
            return False, None
        
        validation = soldier_data_validation(data)
        if validation == data:
            soldier.update(data)

            write_back_to_json(soldiers, f)
            return True, soldier['id']
        
        return False, validation

def delete_soldier(soldier_id: int):
    
    with open(FILE_NAME, 'r+', encoding='utf-8') as f:
        
        soldiers: list = json.load(f)
        soldier: dict = get_soldier_by_id(soldiers, soldier_id)
        if soldier:
            soldiers.remove(soldier)

            write_back_to_json(soldiers, f)
            return True
        return False