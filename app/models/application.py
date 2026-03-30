from sqlalchemy import Column, Integer, String, Date, DateTime
from datetime import datetime
from app.database import Base 


class Application(Base):
	__tablename__ = "applications"

	id = Column(Integer, primary_key=True, index=True)
	reference_number = Column(String, unique=True, index=True)
	address = Column(String, index=True)
	description = Column(String)
	application_type = Column(String)
	status = Column(String, index=True)
	submission_date = Column(Date)
	decision_date = Column(Date, nullable=True)
	created_at = Column(Date, default= datetime.utcnow) 
	