import atexit
import datetime
import os

from sqlalchemy import DateTime, String, Integer, create_engine, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker


POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "secret")
POSTGRES_USER = os.getenv("POSTGRES_USER", "app")
POSTGRES_DB = os.getenv("POSTGRES_DB", "app")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5431")

PG_DSN = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Advert(Base):
    __tablename__ = "app_advert"

    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(
        Integer, unique=False, 
        nullable=False)
    title: Mapped[str] = mapped_column(
        String(100), 
        unique=True, 
        index=True, 
        nullable=False)
    text: Mapped[str] = mapped_column(
        String(1000), 
        unique=True, 
        index=False, 
        nullable=False)
    publication_time: Mapped[datetime.datetime] = mapped_column(
        DateTime, 
        server_default=func.now())

    @property
    def json(self):
        return {
            "id": self.id,
            "author_id": self.author_id,
            "title": self.title,
            "text": self.text,
            "publication_time": self.publication_time.isoformat(),
        }

Base.metadata.create_all(bind=engine)

atexit.register(engine.dispose)
