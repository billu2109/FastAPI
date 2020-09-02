from sqlalchemy import Column,Integer,String
from database import Base

class Jobs(Base):
    __tablename__='Jobs'

    id = Column(Integer, primary_key=True, index=True)
    job_role = Column(String,index=True)
    exp = Column(String,index=True)
    disc = Column(String,index=True)
    loc = Column(String,index=True)


