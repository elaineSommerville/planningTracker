from pydantic import BaseModel
from typing import Optional 

# Schema for the basic application 
class ApplicationBase(BaseModel):
    referemce_number: str
    address: str
    description: str

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