from sqlalchemy.orm import sessionmaker,  DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import os

DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
    class_=AsyncSession,
    expire_on_commit=False
)

Base = DeclarativeBase()

async def get_db():
    async with AsyncSessionLocal() as db:
        try:
            yield db
        finally:
            db.close()


def create_table():
    Base.metadata.create_all(bind=engine)