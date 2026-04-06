from pydantic import BaseModel

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