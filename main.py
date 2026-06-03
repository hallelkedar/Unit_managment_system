from utils import io
from utils.helper import SoldierCreate, SoldierUpdate, SoldierProfile
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from logger_config import logger
import json

app = FastAPI()

@app.exception_handler(HTTPException)
def except_http(req: Request, e: HTTPException):
    logger.error(e.detail)
    return JSONResponse(
        status_code=e.status_code,
        content={"detail": e.detail}
    )

@app.exception_handler(FileNotFoundError)
def except_file_not_found(req: Request, e: FileNotFoundError):
    logger.error(e.msg)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal Server Error"}
        )

@app.exception_handler(json.JSONDecodeError)
def except_json_decode(req: Request, e: json.JSONDecodeError):
    logger.error('Invalid json file')
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal Server Error"}
        )


@app.get('/')
def welcome():
    return {'msg': 'welcome to Unit Personal Management system'}

@app.get('/soldiers', status_code=200)
def get_soldiers():

    logger.info('Try to get soldiers list')
    soldiers = io.get_all_soldiers()
    logger.info('Get soldiers list successfully')
    return soldiers


@app.get('/soldiers/{soldier_id}', status_code=200, response_model=SoldierProfile)
def get_soldier(soldier_id: int):

    logger.info('Try to get soldier')
    soldier = io.get_soldier(soldier_id)
    if soldier:
        logger.info('Soldier return successfully')
        return soldier
    else:
        logger.error('Soldier was not found')
        raise HTTPException(404, 'ID not found')
        

@app.post('/soldiers', status_code=201)
def create_soldier(data: SoldierCreate):

    logger.info('Try to create new soldier')
    soldier_dict = data.model_dump()
    
    new_id = io.create_soldier(soldier_dict)
    
    logger.info('New soldier created.')
    return {'msg': f'New soldier created. (ID:{new_id})'}
    
@app.put('/soldiers/{soldier_id}', status_code=200)
def update_soldier(soldier_id: int, data: SoldierUpdate):
    
    logger.info('Try to update soldier')
    soldier_dict = data.model_dump()
    is_updated = io.update_soldier(soldier_id, soldier_dict)
    
    if not is_updated:
        raise HTTPException(404, 'ID was not found')
    
    logger.info(f'Soldier {soldier_id} updated.')
    return {'msg': f'Soldier - {soldier_id} - updated.'}

@app.delete('/soldiers/{soldier_id}', status_code=200)
def delete_soldier(soldier_id: int):

    logger.info('Try to delete soldier')
    deleted = io.delete_soldier(soldier_id)
    if not deleted:
        raise HTTPException(404, 'ID was not found')
    
    logger.info(f'Soldier {soldier_id} deleted.')
    return {'msg': f'Soldier - {soldier_id} - deleted.'}
