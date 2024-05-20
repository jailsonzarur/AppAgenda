from sqlalchemy import delete, update, select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from uuid import uuid4
from datetime import datetime

class RepositorieEvent:

    def __init__(self, db: Session):
        self.db = db

    def criar(self, event: schemas.Event):
        db_event = models.Event(id=str(uuid4()), name=event.name, 
                                description=event.description, isDone=False, 
                                isCancelled=False, date=datetime.strptime(event.date, '%d/%m/%Y').date(), startTime=event.startTime,
                                endTime=event.endTime)
        
        self.db.add(db_event)
        self.db.commit()
        self.db.refresh(db_event)
        return db_event
    
    def listar(self):
        events = self.db.query(models.Event).all()
        return events
    
    def deletar(self, event_id: str):
        stmt = delete(models.Event).where(models.Event.id==event_id)
        self.db.execute(stmt)
        self.db.commit()
        
    def editar(self, event_id: str, event: schemas.Event):
        stmt = update(models.Event).where(models.Event.id == event_id).values(name=event.name, 
                                                                        description=event.description, startTime=event.startTime,
                                                                        endTime=event.endTime, date=datetime.strptime(event.date, '%d/%m/%Y').date())
        
        self.db.execute(stmt)
        self.db.commit()

    def alterarStatusDone(self, event_id: str):
        event = self.db.query(models.Event).filter(models.Event.id == event_id).first()
        if event.isDone:
            event.isDone = False
        else:
            event.isDone = True
        self.db.commit()

    def alterarStatusCancelled(self, event_id: str):
        event = self.db.query(models.Event).filter(models.Event.id == event_id).first()
        if event.isCancelled:
            event.isCancelled = False
        else:
            event.isCancelled = True
        self.db.commit()