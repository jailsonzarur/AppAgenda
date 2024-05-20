from fastapi import FastAPI, Depends, status
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import criar_bd, get_bd
from src.infra.sqlalchemy.repositories.event import RepositorieEvent


criar_bd()

app = FastAPI()

@app.post('/events')
def criar_evento(event:schemas.Event, db: Session = Depends(get_bd)):
    db_event = RepositorieEvent(db).criar(event)
    return db_event

@app.get('/events')
def listar_eventos(db: Session = Depends(get_bd)):
    events = RepositorieEvent(db).listar()
    return events

@app.delete('/events/{event_id}')
def deletar_evento(event_id: str, db: Session = Depends(get_bd)):
    RepositorieEvent(db).deletar(event_id)
    return {"Message": "Deletado com sucesso!"}

@app.put('/events/{event_id}')
def alterar_propriedade(event_id: str, event: schemas.Event, db: Session = Depends(get_bd)):
    RepositorieEvent(db).editar(event_id, event)
    return {"Message": "Alterado com sucesso!"}

@app.patch('/events/{event_id}/done')
def marcarComoConcluido(event_id: str, db: Session = Depends(get_bd)):
    RepositorieEvent(db).alterarStatusDone(event_id)
    return {"Message": "Alterado com sucesso!"}

@app.patch('/events/{event_id}/cancel')
def marcarComoCancelado(event_id: str, db: Session = Depends(get_bd)):
    RepositorieEvent(db).alterarStatusCancelled(event_id)
    return {"Message": "Alterado com sucesso!"}