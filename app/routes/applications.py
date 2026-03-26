from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services.application_service import get_applications

router = APIRouter()

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
		db,
		status,
		submission_date_from,
		submission_date_to,
		address,
		limit,
		offset,
	)
