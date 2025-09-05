from fastapi import APIRouter

router = APIRouter()


@router.get("/users/all", tags=["users"])
async def get_all_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def get_user_by_username(username: str):
    return {"username": username}


@router.get("/users/{id}", tags=["users"])
async def get_user_by_id(id: int):
    return {"username": id}
