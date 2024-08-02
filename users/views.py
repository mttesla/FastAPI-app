from fastapi import APIRouter

from users import crud
from users.schemas import CreateUser

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
async def create_users(user: CreateUser):
    return crud.create_user(user_in=user)
