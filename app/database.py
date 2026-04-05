from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.orm import declarative_base


DATABASE_URL = "postgresql://postgres:PostBoxGreen@localhost:5432/planning_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

#this is what the route needs
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()



