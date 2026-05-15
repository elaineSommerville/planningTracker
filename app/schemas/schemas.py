from pydantic import BaseModel
from typing import Optional 
from datetime import date 

# Schema for the basic application 
# this is what forms the base of what's returned in JSON 
# this is what the API uses for validation and data transfer 
# PYDANTIC SCHEMA 
# this is how data is sent and validated 
class ApplicationBase(BaseModel):
    reference_number: str
    address: str
    description: str
    application_type: str
    status: str
    submission_date: date 

   
class ApplicationCreate(ApplicationBase):
    pass

class ApplicationOut(ApplicationBase):
    id: int

    class Config:
        from_attributes = True #important (pydantic v2)


# Schema for updating the application
class ApplicationUpdate(BaseModel):
    reference_number: Optional[str] = None
    address: Optional[str] = None
    description: Optional[str] = None 
    application_type: Optional[str] = None
    status: Optional[str] = None 

ApplicationUpdate.model_rebuild() 