from contextlib import asynccontextmanager

from fastapi import FastAPI

import uvicorn

from core.models import Base, db_helper
from items_views import router as items_router
from users.views import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # clean up the ML models and release resources


app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
async def hello_index():
    return {"message": "hello index"}


@app.get("/hello/")
async def hello(name: str = "World"):
    name = name.strip().title()
    return {
        "message": f"hello {name}!",
    }


@app.get("/calc/add/")
async def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
