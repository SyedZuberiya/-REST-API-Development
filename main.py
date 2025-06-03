from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from . import models, schemas, database, crud, tasks

# Create tables if not exist (sync_engine is your synchronous SQLAlchemy engine)
models.Base.metadata.create_all(bind=database.sync_engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI trade app!"}

@app.post("/trades/", response_model=schemas.TradeOut)
def add_trade(trade: schemas.TradeCreate, db: Session = Depends(get_db)):
    new_trade = crud.create_trade(db, trade)
    # Trigger async notification task using Celery
    tasks.send_notification.delay(f"New trade added: {new_trade.ticker}")
    return new_trade

@app.get("/trades/", response_model=List[schemas.TradeOut])
def get_trades(
    ticker: Optional[str] = Query(None),
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    db: Session = Depends(get_db)
):
    return crud.get_trades(db, ticker, start_date, end_date)
