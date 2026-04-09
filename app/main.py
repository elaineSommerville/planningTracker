from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
from enum import Enum
from fastapi import Depends
from app.routes import applications
from app.schemas.schemas import ApplicationOut
from app.schemas.schemas import ApplicationCreate
from app.schemas.schemas import ApplicationUpdate
from app.database import get_db


#TEMPORARY SETUP FOR TABLES
from app.models.application import Base
from app.database import engine
Base.metadata.create_all(bind=engine)

#set the /docs url so it displays correctly 
app = FastAPI(docs_url="/docs") #this is what was missing, i didnt define 'app'
app.include_router(applications.router) #THIS IS REALLY IMPORTANT! 


# initialize an empty applications array
applications = [] 

# message to ensure the server is working
@app.get("/")
def read_root():
	return {"message": "Planning Tracker API running"}

# create status class/type
class Status(str, Enum):
	pending = "pending"
	approved = "approved"
	rejected = "rejected"

# this is the base class which each application is constructed from
class Application(BaseModel):
	id: int
	reference_number: str
	address: str
	description: str
	application_type: Optional[str] = None
	status: Status
	submission_date: date	
	decision_date: Optional[date] = None
	created_at: date_time
	updated_at: Optional[datetime] = None
	limit: Optional[int] = 10
	offset: Optional[int] = 0


# this is the filtering model
# this is a dedicated filter schema instead of stuffing everything into a route
class ApplicationFilter(BaseModel):
	status: Optional[Status] = None
	submission_date_from: Optional[date] = None
	submission_date_to: Optional[date] = None
	decision_date_from: Optional[date] = None
	decision_date_to: Optional[date] = None
	address: Optional[str] = None
	application_type: Optional[str] = None
	limit: Optional[int] = 10 #this adds pagination
	offset: Optional[int] = 0 #this adds paginiation
	sort_by: Optional[str] = "submission_date" #this adds sorting
	order: Optional[str] = "desc" #this orders the sort

