from fastapi import FastAPI

app = FastAPI() #this is what was missing, i didnt define 'app'

@app.get("/")
def read_root():
	return {"message": "Planning Tracker API running"}
