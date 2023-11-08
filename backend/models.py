from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    animal_type = Column(String, index=True)
    age = Column(Integer)
    traits = Column(JSON)

# You will need to call this somewhere to actually create the tables
# Base.metadata.create_all(bind=engine)
