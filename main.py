from utils import io
from utils.helper import SoldierCreate
from fastapi import FastAPI, status, HTTPException
from logger_config import logger
import json

app = FastAPI()

@app.get('/')
def welcome():
    return {'msg': 'welcome to Unit Personal Management system'}

@app.get('/soldiers', status_code=200)
def get_soldiers():
    try:
        logger.info('Try to get soldiers list')
        soldiers = io.get_all_soldiers()
        logger.info('Get soldiers list successfully')
        return soldiers
    
    except FileNotFoundError:
        logger.error('File not found')
    
    except json.JSONDecodeError:
        logger.error('Invalid json file')

    raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Internal Server Error')

@app.get('/soldiers/{soldier_id}', status_code=200)
def get_soldier(soldier_id: int):
    try:
        logger.info('Try to get soldier')
        soldier = io.get_soldier(soldier_id)
        if soldier:
            logger.info('Soldier return successfully')
            return soldier
        else:
            logger.error('Soldier was not found')
            raise HTTPException(404, 'ID not found')
        
    except FileNotFoundError:
        logger.error('File not found')
    
    except json.JSONDecodeError as e:
        logger.error('Invalid json file')
    raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Internal Server Error')

@app.post('/soldiers', status_code=201)
def create_soldier(data: SoldierCreate):
    try:
        logger.info('Try to create new soldier')
        soldier_dict = data.model_dump()
        
        new_id = io.create_soldier(soldier_dict)
        
        logger.info('New soldier created.')
        return {'msg': f'New soldier created. (ID:{new_id})'}

    except FileNotFoundError:
        logger.error('File not found')
    
    except json.JSONDecodeError as e:
        logger.error('Server database file is corrupted')
    
    raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Internal Server Error')
    
@app.put('/soldiers/{soldier_id}', status_code=200)
def update_soldier(soldier_id: int, data: SoldierCreate):
    try:
        logger.info('Try to update soldier')
        soldier_dict = data.model_dump()
        is_updated = io.update_soldier(soldier_id, soldier_dict)
        
        if not is_updated:
            raise HTTPException(404, 'ID was not found')
        
        logger.info(f'Soldier {soldier_id} updated.')
        return {'msg': f'Soldier - {soldier_id} - updated.'}
    
    except FileNotFoundError:
        logger.error('File not found')
        
    except json.JSONDecodeError as e:
        logger.error('Server database file is corrupted')

    raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Internal Server Error')

@app.delete('/soldiers/{soldier_id}', status_code=200)
def delete_soldier(soldier_id: int):
    try:
        logger.info('Try to delete soldier')
        deleted = io.delete_soldier(soldier_id)
        if not deleted:
            raise HTTPException(404, 'ID was not found')
        
        logger.info(f'Soldier {soldier_id} deleted.')
        return {'msg': f'Soldier - {soldier_id} - deleted.'}
    
    except FileNotFoundError:
        logger.error('File not found')
   
    except json.JSONDecodeError as e:
        logger.error('Server database file is corrupted')
    raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Internal Server Error')
