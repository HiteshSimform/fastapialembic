# app/models/user.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy.sql import func


class TestUserr(Base):
    __tablename__ = "testuserss"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
