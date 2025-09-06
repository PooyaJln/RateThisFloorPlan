from fastapi import APIRouter, Depends
from controllers import floor_plans
router = APIRouter()


@router.get("/floorplan/all", tags=["floorplans"])
async def get_all_floorplans():
    resp = 
    return resp


@router.get("/floorplan/{id}", tags=["floorplans"])
async def get_floor_plan_by_id(id: int):
    resp = 
    return resp


@router.put("/floorplan/{id}", tags=["floorplans"])
async def update_floor_plan_by_id(id: int):
    resp = 
    return resp


@router.post("/floorplan/", tags=["floorplans"])
async def create_floor_plan():
    resp = 
    return resp
