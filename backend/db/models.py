from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from db.database import Base

class RequestLog(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    user_input = Column(String)
    ai_output = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)