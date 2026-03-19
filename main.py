from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI() #this is what was missing, i didnt define 'app'

# initialize an empty applications array
applications = [] 

# message to ensure the server is working
@app.get("/")
def read_root():
	return {"message": "Planning Tracker API running"}

class Application(BaseModel):
	id: int
	address: str
	description: str
	status: str
	submission_date: date

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
		
			
