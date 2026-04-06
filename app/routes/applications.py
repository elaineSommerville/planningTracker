from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional 
from datetime import date

from app.database import get_db
from app.services.application_service import get_applications
from app.schemas import ApplicationCreate, ApplicationOut
from app.models import Application
router = APIRouter()

@router.post("/applications/", response_model=ApplicationOut)
def create_application(app: ApplicationCreate, db: Session = Depends(get_db)):
    db_app = Application(**app.dict())
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app

@router.get("/applications")
def read_applications(
	status: str = None,
	submission_date_from: str = None,
	submission_date_to: str = None,
	address: str = None, 
	limit: int = 10,
	offset: int = 0,
	db: Session = Depends(get_db),
):
	return get_applications(
		db = db,
		status = status,
		submission_date_from = submission_date_from,
		submission_date_to = submission_date_to,
		address = address,
		limit = limit,
		offset = offset,
	)
