from sqlalchemy import Column, Integer, String, ForeignKey, Text
from app.database import Base

class Ad(Base):
    __tablename__ = "ads"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(Text)

class Show(Base):
    __tablename__ = "shows"
    id = Column(Integer, primary_key=True)
    ad_id = Column(Integer, ForeignKey("ads.id"))
    user_id = Column(Integer)
