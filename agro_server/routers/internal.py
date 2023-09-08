from fastapi.routing import APIRouter
from agro_server.models.base_router_models import InternalStatistics
import json 
#from settings.logging import base_logger 
from uuid import UUID
from datetime import datetime



internal_router= APIRouter(prefix='/internal')

@internal_router.get('/')
def get_statuses():
    pass
    # TODO: get request body 
    # fastapi.Body()
    # TODO: parse inner json sensors 
    # TODO: map sensor_id to router GET registry_sensors/{device_id}


@internal_router.get('/isalive', tags=['liveness'])
def check_liveness():
    return {'ping_status':'OK'}