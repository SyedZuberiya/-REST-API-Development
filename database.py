from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Async DB URL for async queries (you might not use async now, but good to have)
DATABASE_URL_ASYNC = "postgresql+asyncpg://myuser:Riya%40123@localhost/mydb"

# Sync DB URL for synchronous queries (used for metadata and regular Session)
DATABASE_URL_SYNC = "postgresql://myuser:Riya%40123@localhost/mydb"

# Async engine
engine = create_async_engine(DATABASE_URL_ASYNC, echo=True)

# Async session factory
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

# Sync engine (used for create_all and sync sessions)
sync_engine = create_engine(DATABASE_URL_SYNC, echo=True)

# Sync session factory (IMPORTANT: add this to get DB sessions in main.py)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)

# Base class for models
Base = declarative_base()
