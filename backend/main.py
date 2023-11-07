from fastapi import FastAPI
from data import PETS


app = FastAPI(title="Pet Compatibility API")


@app.get("/")
async def root():
    return {"Testing": "Is this thing on?"}

@app.get("/pets")
async def get_pets():
    return PETS

@app.get("/pets/{id}")
async def get_specific_pet(id: int):
    for pet in PETS:
        if int(pet["id"]) == id:
            return PETS[id - 1]
    return{"body": f"Pet with id {id} was not found :("}

@app.post("/pets")
async def add_pet(pet : dict):
    PETS.append(pet)
    return {"dict": "Pet was added to list!!!"}

@app.put("/pets/{id}")
async def change_pet_traits(id: int, traits: dict ):
    for pet in PETS:
        if int(pet["id"]) == id:
            pet["traits"] = traits["traits"]
            return {"body" : f"Pet with id {id} has been updated!"}
    return {
        "body" : f"Pet with id {id} could not be found"
    }

@app.delete("/pets/{id}")
def remove_pet(id:int):
    for pet in PETS:
        if int(pet["id"]) == id:
            PETS.remove(pet)
            return {"body" : f"Pet with id {id} was removed!"}
    return {"body" : f"pet with id {id} could not be found!"}