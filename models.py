

from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base  # assuming your Base is created in database.py

class Trade(Base):
    __tablename__ = 'trades'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
    side = Column(String)
    timestamp = Column(DateTime)
