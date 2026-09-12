from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from .database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(1024), nullable=True)
    status = Column(String(50), default="pending")  # pending or completed
    created_at = Column(DateTime(timezone=True), server_default=func.now())
