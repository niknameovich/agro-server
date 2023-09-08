from fastapi.routing import APIRouter
from agro_server.models.base_router_models import TelemetryResponseModel
try:
    from settings.logging import base_logger 
    from settings import postgres_config
except Exception as ex:
    print(ex)
from uuid import UUID
from datetime import datetime


telemetry = APIRouter()

@telemetry.post('/{device_id}')
def send_telemetry(request,device_id:UUID):
    pass
    # TODO: get request body 
    # fastapi.Body()
    # TODO: parse inner json sensors 
    # TODO: map sensor_id to router GET registry_sensors/{device_id}

@telemetry.get('/{target_device_id}')
def get_avg_data_for_device(request_date:datetime, sensors:list):
    pass
    # TODO: how to deal with estimate efficency 


@telemetry.get('/isalive', tags=['liveness'])
def check_liveness():
    return {'ping_status':'OK'}

# TODO: add authorization middleware 