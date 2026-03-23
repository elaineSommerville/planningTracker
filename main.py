from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
from enum import Enum
from fastapi import Depends

app = FastAPI() #this is what was missing, i didnt define 'app'

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

# Get Applications
# interviewers like to see this pattern
@app.get("/applications")
def get_applications(filters: ApplicationFilter = Depends()):
	return filter_applications(filters)
 


# create a POST endpoint
# this adds an application of type/model(BaseModel) 'Application' to applications array
@app.post("/applications")
def create_application(application: Application):
	applications.append(application)
	return application

# create a GET endpoint
# this retrieves all of the applications currently in the applications array
@app.get("/applications")
def get_applications():
	return applications

# create a GET endpoint
# this retrieves one application via its id parameter
@app.get("/applications/{app_id}")
def get_application(app_id:int):
	for app in applications:
		if app.id == app_id:
			return app
	return {"error": "Application not found"}

# create a PUT endpoint 
@app.put("/applications/{app_id}")
def update_application(app_id: int, updated_app: Application):
	for index, app in enumerate(applications):
		if app.id == app_id: 
			applications[index] = updated_app
			return updated_app
	return {"error": "Application not found"}
		
# create a DELETE endpoint
@app.delete("/applications/{app_id}")
def delete_application(app_id: int):
	for index, app in enumerate(applications):
		if app.id == app_id:
			deleted_app = applications.pop(index)
			return {"message": "Application deleted", "data": deleted_app}
	return {"error": "Application not found"}

# create a GET endpoint
# get all the applications with a 'status' parameter of 'pending'
@app.get("/applications/{app_status}")
def get_application_status(app_status: str):
	for index, app in enumerate(applications):
		if app.status == app_status:
			status_app = applications.pop(index)
			return {"message": "Pending applications", "data": status_app}
		return {"error": "Pending applications not found"}  			
