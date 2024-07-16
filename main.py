from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr

import uvicorn

from items_views import router as items_router

app = FastAPI()
app.include_router(items_router, prefix='/items_views')


class CreateUser(BaseModel):
    email: EmailStr


@app.get('/')
async def hello_index():
    return { 'message': 'hello index'}


@app.get('/hello/')
async def hello(name: str='World'):
    name = name.strip().title()
    return { 'message': f'hello {name}!',}

    
@app.post('/users/')
async def create_user(user: CreateUser):
    return {
        'message': 'success',
        'email': user.email,
    }
    

@app.get('/calc/add/')
async def add(a: int, b: int):
    return {
        'a': a,
        'b': b, 
        'result': a + b,
    }
    
    



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)