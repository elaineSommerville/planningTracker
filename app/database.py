from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.application import Base
from app.database import engine

Base.metadata.create_all(bind=engine)

# dependencies for FastAPI
#from sqlalchemy.orm import session
#from database import SessionLocal

DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/planning_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


