import os
import json
from logger_config import logger

file_name = 'soldiers.json'

if not os.path.exists(file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        data = []
        json.dump(data, f, indent=2)

def get_soldier_by_id(soldiers: dict, soldier_id: int):
    for soldier in soldiers:
            if soldier['id'] == soldier_id:
                return soldier
    return None

def write_back_to_json(data, file):
    file.seek(0)
    json.dump(data, file, indent=2)
    file.truncate()
    
def get_all_soldiers():
    
    with open(file_name, 'r', encoding='utf-8') as f:
        soldiers = json.load(f)
        logger.info('Open soldiers json file, Get dict')
        
        if len(soldiers) == 0:
            logger.warning('Soldiers list is empty.')
        
        return soldiers

def get_soldier(soldier_id: int):
    
    with open(file_name, 'r', encoding='utf-8') as f:
        soldiers = json.load(f)
        
        return get_soldier_by_id(soldiers, soldier_id)
    return None
    
def create_soldier(data: dict):
    with open(file_name, 'r+', encoding='utf-8') as f:
        logger.info('Try to create new soldier')
        soldiers: list = json.load(f)
        data['id'] = max(soldiers) + 1 if soldiers else 1
        soldiers.append(data)
        
        write_back_to_json(soldiers, f)
        logger.info('New soldier created.')
        
        return True

def update_soldier(soldier_id: int, data: dict):
    with open(file_name, 'r+', encoding='utf-8') as f:
        logger.info('Try to update soldier')
        soldiers = json.load(f)
        soldier:dict = get_soldier_by_id(soldiers, soldier_id)
        if soldier:
            soldier.update(data)

            write_back_to_json(soldiers, f)
            logger.info(f'Soldier {soldier['id']} updated.')
            return True
        return False

def delete_soldier(soldier_id):
    with open(file_name, 'r+', encoding='utf-8') as f:
        logger.info('Try to delete soldier')
        soldiers: list = json.load(f)
        soldier: dict = get_soldier_by_id(soldiers, soldier_id)
        if soldier:
            soldiers.remove(soldier)

            write_back_to_json(soldiers, f)
            logger.info(f'Soldier {soldier['id']} deleted.')
            return True
        return False