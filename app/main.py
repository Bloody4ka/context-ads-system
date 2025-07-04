from fastapi import FastAPI
from app import models, database
from app.ads import router as ads_router

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(ads_router)
