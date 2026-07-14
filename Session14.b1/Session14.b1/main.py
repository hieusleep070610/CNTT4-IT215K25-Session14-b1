from fastapi import FastAPI

from database import Base
from database import engine

from routers.product import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)