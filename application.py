from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Application(Base):
	_tablename_ = "application"

	id: Column(Integer, primary_key=True, index=True
	reference_number = Column(String, unique=True, index=True)
	address = Column(String, index=True)
	description = Column(String)
	application_type = Column(String)
	status = Column(String, index=True)
	submission_date = Column(Date)
	decision_date = Column(Date, nullable=True)
	created_at = Column(Date, default= datetime.utcnow) 
