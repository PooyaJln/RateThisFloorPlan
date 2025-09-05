from fastapi import APIRouter

router = APIRouter()


@router.get("/floorplan/all", tags=["floorplans"])
async def get_all_floorplans():
    return [{"floorplan": "Rick"}, {"floorplan": "Morty"}]


@router.get("/floorplan/{id}", tags=["floorplans"])
async def get_floor_plan_by_id(id: int):
    return {"floorplan": id}


@router.put("/floorplan/{id}", tags=["floorplans"])
async def update_floor_plan_by_id(id: int):
    return {"floorplan": id}


@router.post("/floorplan/", tags=["floorplans"])
async def create_floor_plan():
    return {"floorplan": id}
