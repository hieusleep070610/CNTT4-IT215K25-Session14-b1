from fastapi import FastAPI

from database import Base, engine
from routers.product import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Product Management API"
)

app.include_router(router)