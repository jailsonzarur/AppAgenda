from src.infra.sqlalchemy.config.database import Base
from sqlalchemy import Column, String, Boolean, Integer, Date

class Event(Base):
    __tablename__ = 'events'

    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    isDone = Column(Boolean)
    isCancelled = Column(Boolean)
    date = Column(Date)
    startTime = Column(Integer)
    endTime = Column(String)