from fastapi import FastAPI
from .routers import well

app = FastAPI()

app.include_router(well.router, prefix="/api", tags=["wells"])