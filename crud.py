from sqlalchemy.orm import Session
import models, schemas


def update_job(db:Session, jobs_id: int, job: schemas.Jobs):
    db_job = db.query(models.Jobs).filter(models.Jobs.id == jobs_id).first()
    db_job.job_role = job.job_role
    db_job.exp = job.exp
    db_job.disc = job.disc
    db_job.loc = job.loc
    db.commit()
    db.refresh(db_job)
    return db_job

def delete_job(db: Session, jobs_id: int):
    db_job = db.query(models.Jobs).filter(models.Jobs.id == jobs_id).first()
    db.delete(db_job)
    db.commit()
