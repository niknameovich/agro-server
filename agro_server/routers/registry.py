from fastapi.routing import APIRouter
from agro_server.models.base_router_models import Sensor
import json 
#from settings.logging import base_logger 
from uuid import UUID
from datetime import datetime



registry = APIRouter()

@registry.get('/{device_id}')
def get_sensor_spec_for_device(device_id:UUID, sensor_tyoe_id:int):
    pass
    # TODO: get url params 
    # TODO: select * from DB.device_sensors where device_id = url.device_id
    # OR 
    # select * from sensor_types where type_id = sensor_type_id 
    # left join  DB.device_sensors using(sensor_id) and device_id = device_id

@registry.post('/{device_id}')
def append_new_sensor_to_device(device_id:UUID, sensor:Sensor):
    pass
    # TODO: check device_existance 
    # TODO: insert into device_sensors (target_device_id, created_at ...) 
    # ... - get sensor_type from sensor_types or request

@registry.put('/{prev_device_id}/{target_device_id}')
def move_sensor_to_other_device(prev_device_id,target_device_id, sensor_id, move_device:bool=False):
    pass 
    # TODO: update device relation to any 

@registry.delete('/{device_id}')
def delete_device_from_location(device_id,location_id:int=None, move_telemetry_to_trash_too:bool=False):
    pass 
    # TODO: check device existance at all or in location_id  
    # TODO: CASCADE DELETE from device_location, device_mechanisms, if move_telemetry_to_trash_too: device_telemetry, device_actions, devices


@registry.get('/isalive', tags=['liveness'])
def check_liveness():
    return {'ping_status':'OK'}

# TODO: add authorization middleware 