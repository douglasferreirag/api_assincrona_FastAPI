from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from src.database import Base
from sqlalchemy import select

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    balance = Column(Float, default=0.0)

    # relationship with transactions (not strictly needed for queries)
    transactions = relationship("Transaction", back_populates="account", cascade="all, delete-orphan")



