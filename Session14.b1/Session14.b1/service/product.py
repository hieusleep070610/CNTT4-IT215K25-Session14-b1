from sqlalchemy.orm import Session

from models.product import Product
from schemas.product import ProductCreate


def get_all_products_service(db: Session):
    return db.query(Product).all()


def get_product_by_id_service(
        product_id: int,
        db: Session
):
    return db.query(Product).filter(
        Product.id == product_id
    ).first()


def create_product_service(
        product: ProductCreate,
        db: Session
):
    try:
        new_product = Product(
            name=product.name,
            price=product.price
        )

        db.add(new_product)
        db.commit()
        db.refresh(new_product)

        return new_product

    except Exception:
        db.rollback()
        raise


def update_product_service(
        product_id: int,
        product: ProductCreate,
        db: Session
):
    try:
        product_in_db = db.query(Product).filter(
            Product.id == product_id
        ).first()

        if not product_in_db:
            return None

        product_in_db.name = product.name
        product_in_db.price = product.price

        db.commit()
        db.refresh(product_in_db)

        return product_in_db

    except Exception:
        db.rollback()
        raise


def delete_product_service(
        product_id: int,
        db: Session
):
    try:
        product_in_db = db.query(Product).filter(
            Product.id == product_id
        ).first()

        if not product_in_db:
            return None

        db.delete(product_in_db)
        db.commit()

        return product_in_db

    except Exception:
        db.rollback()
        raise