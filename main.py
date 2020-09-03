from typing import List
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

import crud
import database
import models, schemas
from fastapi import FastAPI, Depends
from database import engine, SessionLocal
from models import Jobs

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


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/jobs", response_model=List[schemas.Jobs])
def show_records(db: Session = Depends(get_db)):
    records = db.query(models.Jobs).all()
    return records


@app.post("/job")
async def Job_post(job_request: JobRequest, db: Session = Depends(get_db)):
    job = Jobs()
    job.job_role = job_request.job_role
    job.exp = job_request.exp
    job.disc = job_request.disc
    job.loc = job_request.loc

    db.add(job)
    db.commit()

    return {
        'code': 'success',
        'massage': 'Job Post Created'
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
async def delete_data(jobs_id: int,db: Session = Depends(get_db)):
    crud.delete_job(db=db, jobs_id=jobs_id)
    return {
        'code': 'success ',
        'massage': 'Job Post successfully deleted'
    }