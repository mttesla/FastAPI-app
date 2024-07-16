from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr

import uvicorn

from items_views import router as items_router
from users.views import router as user_router


app = FastAPI()
app.include_router(items_router)
app.include_router(user_router)


@app.get('/')
async def hello_index():
    return { 'message': 'hello index'}


@app.get('/hello/')
async def hello(name: str='World'):
    name = name.strip().title()
    return { 'message': f'hello {name}!',}



@app.get('/calc/add/')
async def add(a: int, b: int):
    return {
        'a': a,
        'b': b, 
        'result': a + b,
    }
    

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)