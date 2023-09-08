
from fastapi.routing import APIRouter
from agro_server.models.base_router_models import Actions
import json 
try:
    from settings.logging import base_logger 
    from settings import postgres_config
except Exception as ex:
    print(ex)

from datetime import datetime



actions_router = APIRouter(
    prefix='/actions',
    tags=['custom', 'base']
    )

@actions_router.post('/{device_id}/{type_id}/}')
def append_new_task_to_device(device_id,type_id, action_obj:Actions):
    pass
    # TODO: get request body 
    # fastapi.Body()
    # TODO: parse url params  
    # TODO: update/insert device_actions set valid_until, target_value 
    # if device_id = None - get all relative sensors in current location, create tasks to all relative devices  

@actions_router.get('/{device_id}')
def get_current_device_schedule(request_date:datetime, sensor_id):
    pass
    # TODO: update schedule on device 


@actions_router.get('/isalive', tags=['liveness'])
def check_liveness():
    return {'ping_status':'OK'}




# TODO: add authorization middleware 