from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request

from sqlalchemy.orm import Session

from database import get_db

from utils.response import create_response

from schemas.product import ProductCreate

from service.product import (
    get_all_products_service,
    get_product_by_id_service,
    create_product_service,
    update_product_service,
    delete_product_service
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/")
def get_products(
        request: Request,
        db: Session = Depends(get_db)
):
    products = get_all_products_service(db)

    return create_response(
        status_code=200,
        message="Get all products successfully",
        path=request.url.path,
        data=products
    )


@router.get("/{product_id}")
def get_product(
        product_id: int,
        request: Request,
        db: Session = Depends(get_db)
):
    product = get_product_by_id_service(
        product_id,
        db
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return create_response(
        status_code=200,
        message="Get product successfully",
        path=request.url.path,
        data=product
    )


@router.post("/")
def create_product(
        product: ProductCreate,
        request: Request,
        db: Session = Depends(get_db)
):
    new_product = create_product_service(
        product,
        db
    )

    return create_response(
        status_code=201,
        message="Create product successfully",
        path=request.url.path,
        data=new_product
    )


@router.put("/{product_id}")
def update_product(
        product_id: int,
        product: ProductCreate,
        request: Request,
        db: Session = Depends(get_db)
):
    updated_product = update_product_service(
        product_id,
        product,
        db
    )

    if not updated_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return create_response(
        status_code=200,
        message="Update product successfully",
        path=request.url.path,
        data=updated_product
    )


@router.delete("/{product_id}")
def delete_product(
        product_id: int,
        request: Request,
        db: Session = Depends(get_db)
):
    deleted_product = delete_product_service(
        product_id,
        db
    )

    if not deleted_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return create_response(
        status_code=200,
        message="Delete product successfully",
        path=request.url.path,
        data=deleted_product
    )