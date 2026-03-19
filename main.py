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
