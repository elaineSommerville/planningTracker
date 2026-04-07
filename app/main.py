from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
from enum import Enum
from fastapi import Depends
from app.routes import applications
#from app.schemas import ApplicationsCreate 
from app.schemas import ApplicationOut


#TEMPORARY SETUP FOR TABLES
from app.models.application import Base
from app.database import engine
Base.metadata.create_all(bind=engine)

#set the /docs url so it displays correctly 
app = FastAPI(docs_url="/docs") #this is what was missing, i didnt define 'app'
#app.include_router(applications.router)

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

# Get Applications
# interviewers like to see this pattern
@app.get("/applications")
def get_applications(filters: ApplicationFilter = Depends()):
	return filter_applications(filters)
 
# building the filtering logic
def filter_applications(filters: ApplicationFilter):
	query = "SELECT * FROM applications WHERE 1=1"
	params = {}

	if filters.status:
		query += "AND status = :status"
		params["submission_date_from"] = filters.submission_date_from

	if filters.submission_date_to:
		query += "AND submission_date <= :submission_date_to"
		params["submission_date"] = filters.submission_date_to

	if filters.address:
		query += "AND address ILIKE :address"
		params["address"] = f"%{filters.address}%"

	query += " LIMIT :limit OFFSET :offset"
	params["limit"] = filters.limit
	params["offset"] = filters.offset
	
	query += f" ORDER BY {filters.sort_by} {filters.order}"

	return execute_query(query, params)

# # ___start or original CRUD enpoints___
# # create a POST endpoint
# # this adds an application of type/model(BaseModel) 'Application' to applications array
# @app.post("/applications")
# def create_application(ApplicationCreate):
# 	applications.append(application)
# 	return application

# # create a GET endpoint
# # this retrieves all of the applications currently in the applications array
# @app.get("/applications")
# def get_applications():
# 	return applications

# # create a GET endpoint
# # this retrieves one application via its id parameter
# @app.get("/applications/{app_id}")
# def get_application(app_id:int):
# 	for app in applications:
# 		if app.id == app_id:
# 			return app
# 	return {"error": "Application not found"}

# # create a PUT endpoint 
# @app.put("/applications/{app_id}")
# def update_application(app_id: int, updated_app: Application):
# 	for index, app in enumerate(applications):
# 		if app.id == app_id: 
# 			applications[index] = updated_app
# 			return updated_app
# 	return {"error": "Application not found"}
		
# # create a DELETE endpoint
# @app.delete("/applications/{app_id}")
# def delete_application(app_id: int):
# 	for index, app in enumerate(applications):
# 		if app.id == app_id:
# 			deleted_app = applications.pop(index)
# 			return {"message": "Application deleted", "data": deleted_app}
# 	return {"error": "Application not found"}

# # create a GET endpoint
# # get all the applications with a 'status' parameter of 'pending'
# @app.get("/applications/{app_status}")
# def get_application_status(app_status: str):
# 	for index, app in enumerate(applications):
# 		if app.status == app_status:
# 			status_app = applications.pop(index)
# 			return {"message": "Pending applications", "data": status_app}
# 		return {"error": "Pending applications not found"}  			
