from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

@router.get("/ads", response_model=list[schemas.AdOut])
def get_ads(db: Session = Depends(database.SessionLocal)):
    return db.query(models.Ad).all()
