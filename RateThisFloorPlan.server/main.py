from fastapi import FastAPI

from routers import floor_plans, users

app = FastAPI()
app.title = "Rate this Floor Plan"


app.include_router(users.router)
app.include_router(floor_plans.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
