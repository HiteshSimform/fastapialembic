# app/models/author.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy.sql import func


class NewAuthor(Base):
    __tablename__ = "newauthors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    country = Column(String(50))

    books = relationship("Book", back_populates="author", cascade="all, delete")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
