
from pydantic import BaseModel





class Jobs(BaseModel):
    id: int
    job_role: str
    exp: str
    disc: str
    loc: str

    class Config:
        orm_mode = True

