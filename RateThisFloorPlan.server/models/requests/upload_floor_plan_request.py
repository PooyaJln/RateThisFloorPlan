from pydantic import BaseModel


class UploadRentalFloorPlanRequest(BaseModel):
    address: str
    owner: str
    architect_co: str | None = None


class UploadAgandesRattFloorPlanRequest(BaseModel):
    new_construct: bool
    project_name: str
    construct_co: str | None = None
    architect_co: str | None = None
