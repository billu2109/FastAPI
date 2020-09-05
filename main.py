from typing import List, Optional
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy.orm import Session
import crud
import models, schemas
from fastapi import FastAPI, Depends, UploadFile, File, Request
from database import engine, SessionLocal
from models import Jobs,Apply_Job

models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")


app = FastAPI()


class JobRequest(BaseModel):
    job_role: str
    exp: str
    disc: str
    loc: str
    class Config:
        orm_mode = True

class Apply(BaseModel):
    name: str
    mobile_number: str
    email: str

    class Config:
        orm_mode = True



def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



@app.get("/jobs/{ Jobs_id }", response_model=List[schemas.Jobs])
def show_records( db: Session = Depends(get_db)):
    records = db.query(models.Jobs).all()
    Jobs_id = Jobs.id
    return records

@app.post("/job")
async def Job_post(job_request: JobRequest, db: Session = Depends(get_db)
):
    job = Jobs()
    job.job_role = job_request.job_role
    job.exp = job_request.exp
    job.disc = job_request.disc
    job.loc = job_request.loc

    db.add(job)
    db.commit()


    return {
        'code': 'success',
        'massage': 'Job Post Created',

    }


@app.put("/job/{jobs_id}")
async def update_job(jobs_id: int, job: schemas.Jobs, db: Session = Depends(get_db)):
    crud.update_job(db=db, jobs_id=jobs_id, job=job)
    return {
        'code': 'success ',
        'massage': 'Job Post successfully updated'
    }


@app.patch("/job/{jobs_id}")
async def update_job(jobs_id: int, job: schemas.Jobs, db: Session = Depends(get_db)):
    crud.update_job(db=db, jobs_id=jobs_id, job=job)
    return {
        'code': 'success ',
        'massage': 'Job Post successfully updated'
    }


@app.delete("/job/{ jobs_id }")
async def delete_data(jobs_id: int, db: Session = Depends(get_db)):
    crud.delete_job(db=db, jobs_id=jobs_id)
    return {
        'code': 'success ',
        'massage': 'Job Post successfully deleted'
    }


# Job Application form

@app.post("/apply/job")
async def apply_job(job_req: Apply, db: Session = Depends(get_db),resume: List[UploadFile] = File(...)):
    apply_job = Apply_Job()
    apply_job.name = job_req.name
    apply_job.mobile_number = job_req.mobile_number
    apply_job.email = job_req.email
    resume = db.query(resume)
    db.add(apply_job)
    db.commit()

    return {
        'code': 'success',
        'massage': 'Job Post Created'
    }
