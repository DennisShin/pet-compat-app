from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from . import crud, models, schemas, database
from fastapi.templating import Jinja2Templates
from pathlib import Path

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Pet Compatability API")
BASE_PATH = Path(__file__).resolve().parent
templates = Jinja2Templates(directory= str(BASE_PATH / "templates"))

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def home():
    return {"testing": "Is this thing on?"}

@app.post("/pets/", response_model=schemas.Pet)
def create_pet(pet: schemas.PetCreate, db: Session = Depends(get_db)):
    return crud.create_pet(db=db, pet=pet)

# @app.get("/pets/")
# def read_pets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     pets = crud.get_pets(db, skip=skip, limit=limit)
#     return pets

@app.get("/pets/api")
def show_pets(db: Session = Depends(get_db)):
    pets = crud.get_pets(db)
    return pets

@app.get("/pets/", response_class=HTMLResponse)
def show_pets(request: Request, db: Session = Depends(get_db)):
    pets = crud.get_pets(db)
    return templates.TemplateResponse("pets.html", {"request": request, "pets": pets})

@app.get("/pets/{pet_id}", response_model=schemas.Pet, response_class=HTMLResponse)
def read_pet(request: Request, pet_id: int, db: Session = Depends(get_db)):
    db_pet = crud.get_pet(db, pet_id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return templates.TemplateResponse("pet.html", {"request": request, "pet": db_pet})

@app.get("/pets/{pet_id}/api", response_model=schemas.Pet)
def read_pet(pet_id: int, db: Session = Depends(get_db)):
    db_pet = crud.get_pet(db, pet_id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return db_pet

@app.delete("/pets/{pet_id}")
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    pet_info = crud.get_pet(db, pet_id=pet_id)
    deleted = crud.delete_pet(db, pet_id=pet_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Pet not found")
    return {"detail": f"{pet_info.name} deleted successfully"}



# PETS =[
#     {
#       "id": 1,
#       "name": "Fido",
#       "animal_type": "Dog",
#       "age": 3,
#       "traits": ["friendly", "energetic", "playful"]
#     },
#     {
#       "id": 2,
#       "name": "Whiskers",
#       "animal_type": "Cat",
#       "age": 5,
#       "traits": ["independent", "curious"]
#     }
#   ]
# @app.get("/")
# async def root():
#     return {"Testing": "Is this thing on?"}

# @app.get("/pets")
# async def get_pets():
#     return PETS

# @app.get("/pets/{id}")
# async def get_specific_pet(id: int):
#     for pet in PETS:
#         if int(pet["id"]) == id:
#             return PETS[id - 1]
#     return{"body": f"Pet with id {id} was not found :("}

# @app.post("/pets")
# async def add_pet(pet : dict):
#     PETS.append(pet)
#     return {"dict": "Pet was added to list!!!"}

# @app.put("/pets/{id}")
# async def change_pet_traits(id: int, traits: dict ):
#     for pet in PETS:
#         if int(pet["id"]) == id:
#             pet["traits"] = traits["traits"]
#             return {"body" : f"Pet with id {id} has been updated!"}
#     return {
#         "body" : f"Pet with id {id} could not be found"
#     }

# @app.delete("/pets/{id}")
# def remove_pet(id:int):
#     for pet in PETS:
#         if int(pet["id"]) == id:
#             PETS.remove(pet)
#             return {"body" : f"Pet with id {id} was removed!"}
#     return {"body" : f"pet with id {id} could not be found!"}