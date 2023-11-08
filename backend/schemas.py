from pydantic import BaseModel
from typing import List

class PetBase(BaseModel):
    name: str
    animal_type: str
    age: int
    traits: List[str]  # This will be a comma-separated list of traits

class PetCreate(PetBase):
    pass

class Pet(PetBase):
    id: int
