# app/models/book.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db import Base
from models.genre import book_genre
from sqlalchemy.sql import func


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)

    author_id = Column(Integer, ForeignKey("authors.id", ondelete="CASCADE"))
    author = relationship("Author", back_populates="books")

    genres = relationship("Genre", secondary=book_genre, back_populates="books")

    borrowed_by = relationship(
        "BorrowedBook", back_populates="book", cascade="all, delete"
    )

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
