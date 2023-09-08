from pydantic import BaseModel
from typing import Union
from uuid import UUID
from datetime import datetime


"""
Actions response class
"""
class Actions(BaseModel):
    id:UUID
    resposne_datetime:datetime
    status:int


"""
Base telemetry response class
"""
class Device(BaseModel):
    id:UUID
    resposne_datetime:datetime
    status:int
    sensor_spec:dict
    parent_device_id:int


    """
Base telemetry response class
"""
class InternalStatistics(BaseModel):
    id:UUID
    resposne_datetime:datetime
    status:int



"""
Base registry response class
"""
# TODO: move all response classes to folder RESPONSE_CLASSES
class Sensor(BaseModel):
    id:UUID
    resposne_datetime:datetime
    status:int


"""
Base telemetry response class
"""
class TelemetryResponseModel(BaseModel):
    id:UUID
    resposne_datetime:datetime
    status:int