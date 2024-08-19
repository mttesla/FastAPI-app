from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud

from .schemas import Product, ProductCreate
from core.config import settings
from core.models import db_helper
from core.models.db_helper import DatabaseHelper
from .dependencies import product_by_id

router = APIRouter(tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}/", response_model=Product)
async def get_product(
    product=Depends(product_by_id),
):
    return product


@router.put("/{product_id}/")
async def update_product():
    pass


db_helper = DatabaseHelper(url=settings.db_url, echo=settings.db_echo)
