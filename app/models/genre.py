# app/models/genre.py
from sqlalchemy import Column, Integer, String, Table, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db import Base
from sqlalchemy.sql import func
# Many-to-Many association table
book_genre = Table(
    'book_genre',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id', ondelete="CASCADE")),
    Column('genre_id', Integer, ForeignKey('genres.id', ondelete="CASCADE"))
)

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    books = relationship("Book", secondary=book_genre, back_populates="genres")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
