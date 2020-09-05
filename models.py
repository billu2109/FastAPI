from dataclasses import Field

from fastapi import UploadFile
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship

from database import Base



class Apply_Job(Base):
    __tablename__ = "Apply_Job"

    id = Column(Integer,primary_key=True, index=True)
    name = Column(String, index=True )
    mobile_number = Column(String, index=True)
    email = Column(String, index=True)


class Jobs(Base):
    __tablename__='Jobs'

    id = Column(Integer, primary_key=True, index=True)
    job_role = Column(String,index=True)
    exp = Column(String,index=True)
    disc = Column(String,index=True)
    loc = Column(String,index=True)

