from utils import io
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
        raise HTTPException(500, 'Internal Server Error')
    
    except json.JSONDecodeError as e:
        logger.error('Invalid json file')
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Internal Server Error')

@app.post('/soldiers', status_code=201)
def create_soldier(data: dict):
    try:
        logger.info('Try to create new soldier')
        is_create, value = io.create_soldier(data)
        
        if not is_create:
            logger.error('Soldier was not created, Invalid soldier data')
            raise HTTPException(422, f'Invalid Field: {value[0]}, Error: {value[1]}')
        
        logger.info('New soldier created.')
        return {'msg': f'New soldier created. (ID:{value})'}

    except FileNotFoundError:
        logger.error('File not found')
        raise HTTPException(500, 'Internal Server Error')
    
    except json.JSONDecodeError as e:
        logger.error('Server database file is corrupted')
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Internal Server Error')
    
@app.put('/soldiers/{soldier_id}', status_code=200)
def update_soldier(soldier_id: int, data: dict):
    try:
        logger.info('Try to update soldier')
        is_updated, value = io.update_soldier(soldier_id, data)
        
        if not is_updated:
            if value:
                raise HTTPException(422, f'Invalid Field: {value[0]}, Error: {value[1]}')
            raise HTTPException(404, 'ID was not found')
        
        logger.info(f'Soldier {value} updated.')
        return {'msg': f'Soldier - {soldier_id} - updated.'}
    
    except FileNotFoundError:
        logger.error('File not found')
        raise HTTPException(500, 'Internal Server Error')
    
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
        raise HTTPException(500, 'Internal Server Error')
   
    except json.JSONDecodeError as e:
        logger.error('Server database file is corrupted')
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Internal Server Error')
