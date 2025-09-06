from fastapi import Depends, Request


async def get_all_floorplans():
    return [{"floorplan": "Rick"}, {"floorplan": "Morty"}]


async def get_floor_plan_by_id(id: int):
    return {"floorplan": id}


async def update_floor_plan_by_id(request: Request):
    return {"floorplan": request.id}


async def create_floor_plan(request: Request):
    return {"floorplan": request.id}
