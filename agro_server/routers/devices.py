from agro_server.models.base_router_models import Device
from fastapi.routing import APIRouter
import json 
#from settings.logging import base_logger 
from uuid import UUID
from datetime import datetime


device = APIRouter(prefix='/devices')


@device.post('/')
def create_device(device:Device):
    # TODO: insert new device to Postgre.device table with LOCATION 
    if device.sensor_spec:
        for sensor_key, sensor_type in device.sensor_spec.items:
            pass 
    # TODO: create upsert command to POSTGRE 

@device.get('/{target_device_id}')
def get_avg_data_for_device(target_device_id:UUID,request_date:datetime, sensors:list):
    pass
    # TODO: how to deal with estimate efficency 


@device.get('/isalive', tags=['liveness'])
def check_liveness():
    return {'ping_status':'OK'}

# TODO: add authorization middleware 