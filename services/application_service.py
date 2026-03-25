from sqlalchemy.orm inport Session
from models.application import Application
from typing import Optional
from datetime import date

def get_applications(
	db: Session,
	status: Optional[str] = None,
	submission_date_from: Optional[date] = None,
	submission_date_to: Optional[date] = None,
	address: Optional[str] = None,
	limit: int = 10, 
	offset: int = 0,
):
	query - db.query(Application)

	if status:
		query = query.filter(Application.status == status)

	if submission_date_from:
		query = query.filter(Application.submission_date_from >= submission_date_from)

	if submission_date_to:
		query = query.filter(Application.submission_date_to <= submission_date_to)

	if address:
		query = query.filter(Application.address.ilike(f"%{address}%"))

	return query.offset(offset).limit(limit).all()
