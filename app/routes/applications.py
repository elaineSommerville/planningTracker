from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional 
from datetime import date
# routes need access to the db 
from app.database import get_db
#from app.services.application_service import get_applications
from app.schemas import ApplicationCreate, ApplicationOut
from app.schemas.schemas import ApplicationUpdate 
from app.models import Application
router = APIRouter()

@router.post("/applications/", response_model=ApplicationOut)
def create_application(
    application: ApplicationCreate, 
    db: Session = Depends(get_db)
	):
    
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

@router.post("/applications")
def create_application(app: ApplicationCreate, db: Session = Depends(get_db)):
    new_app = Application(**app.dict())
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app

@router.get("/applications")
def get_applications(db: Session = Depends(get_db)):
    return db.query(Application).all()

@router.get("/applications/{app_id}")
def get_application(app_id: int, db: Session = Depends(get_db)):
    return db.query(Application).filter(Application.id == app_id).first()

@router.put("/applications/{app_id}")
def update_application(app_id: int, updated_app: ApplicationUpdate, db: Session = Depends(get_db)):
    app = db.query(Application).filter(Application.id == app_id).first()

    for key, value in updated_app.dict().items():
        setattr(app, key, value)

    db.commit()
    db.refresh(app)
    return app

@router.delete("/applications/{app_id}")
def delete_application(app_id: int, db: Session = Depends(get_db)):
    app = db.query(Application).filter(Application.id == app_id).first()
    db.delete(app)
    db.commit()
    return {"message": "Deleted"}







	# ____BROUGHT IN FROM MAIN.PY TO KEEP IT CLEAN & FREE OF ENDPOINTS____
	# Get Applications
# interviewers like to see this pattern
# @app.get("/applications")
# def get_applications(filters: ApplicationFilter = Depends()):
# 	return filter_applications(filters)
 
# # building the filtering logic
# def filter_applications(filters: ApplicationFilter):
# 	query = "SELECT * FROM applications WHERE 1=1"
# 	params = {}

# 	if filters.status:
# 		query += "AND status = :status"
# 		params["submission_date_from"] = filters.submission_date_from

# 	if filters.submission_date_to:
# 		query += "AND submission_date <= :submission_date_to"
# 		params["submission_date"] = filters.submission_date_to

# 	if filters.address:
# 		query += "AND address ILIKE :address"
# 		params["address"] = f"%{filters.address}%"

# 	query += " LIMIT :limit OFFSET :offset"
# 	params["limit"] = filters.limit
# 	params["offset"] = filters.offset
	
# 	query += f" ORDER BY {filters.sort_by} {filters.order}"

# 	return execute_query(query, params)

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
# # this was breaking /docs previously
# # ensure there is a schema which correlates to this endpoint
# # FIX - created a corresponding schema in schemas.py - called ApplicationUpdate
# @app.put("/applications/{app_id}", response_model=ApplicationOut)
# def update_application(
# 	app_id: int, 
# 	updated_app: ApplicationUpdate,
# 	db: Session = Depends(get_db)
# ):
# 	db_app = db.query(Application).filter(Application.id == app_id).first()
	
# 	if not db_app: 
# 			return {"error": "Application not found"}
# 	for key, value in updated_app.dict(exclude_unset=True).items():
# 		setattr(db_app, key, value)
# 	db.commit()
# 	db.refresh(db_app)

# 	return db_app
		
# # # create a DELETE endpoint
# # @app.delete("/applications/{app_id}")
# # def delete_application(app_id: int):
# # 	for index, app in enumerate(applications):
# # 		if app.id == app_id:
# # 			deleted_app = applications.pop(index)
# # 			return {"message": "Application deleted", "data": deleted_app}
# # 	return {"error": "Application not found"}

# # # create a GET endpoint
# # # get all the applications with a 'status' parameter of 'pending'
# # @app.get("/applications/{app_status}")
# # def get_application_status(app_status: str):
# # 	for index, app in enumerate(applications):
# # 		if app.status == app_status:
# # 			status_app = applications.pop(index)
# # 			return {"message": "Pending applications", "data": status_app}
# # 		return {"error": "Pending applications not found"}  			
 

