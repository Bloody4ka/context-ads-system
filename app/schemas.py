from pydantic import BaseModel

class AdBase(BaseModel):
    title: str
    text: str

class AdCreate(AdBase):
    pass

class AdOut(AdBase):
    id: int
    class Config:
        orm_mode = True
