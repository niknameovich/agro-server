from fastapi import FastAPI, Request, APIRouter
from fastapi.routing import APIRoute
import agro_server.routers as routers
import pkgutil 
from importlib import import_module
from uuid import UUID
from datetime import datetime
import inspect

app = FastAPI()



@app.on_event('startup')
async def on_startup():
    for _,module_name,_ in pkgutil.iter_modules(routers.__path__):
        module = import_module(f"{routers.__name__}.{module_name}")
        module_routers = [item for item in inspect.getmembers(module) if isinstance(item[1],APIRouter)]
        if module_routers:
            for router_name,router_obj in module_routers:
                app.include_router(router_obj, prefix=f'{"/"+router_name if router_obj.prefix == "" else router_obj.prefix}')



@app.get("/url-list-from-request")
def get_all_urls_from_request(request: Request):
    url_list = [
        {"path": route.path, "name": route.name, "tags":route.tags} for route in request.app.router.routes
          if isinstance(route, APIRoute)
    ]
    return url_list



        

