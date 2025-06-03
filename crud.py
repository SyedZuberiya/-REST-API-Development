from sqlalchemy.orm import Session
from . import models, schemas
from typing import List
from datetime import datetime

def create_trade(db: Session, trade: schemas.TradeCreate):
    db_trade = models.Trade(**trade.dict())
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade

def get_trades(db: Session, ticker: str = None, start_date: datetime = None, end_date: datetime = None):
    query = db.query(models.Trade)
    if ticker:
        query = query.filter(models.Trade.ticker == ticker)
    if start_date:
        query = query.filter(models.Trade.timestamp >= start_date)
    if end_date:
        query = query.filter(models.Trade.timestamp <= end_date)
    return query.all()
