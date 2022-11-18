#Librerias

#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI, Query

#Modelo
class Item(BaseModel): #item extiende de basemodel
    name: str
    description: str |None = None #Atributos opcionales
    price: float
    tax: float | None = None

#Instancia
app = FastAPI()

"""prueba

@app.get("/saludo")
def root():
    return {
        
        "Hola": "Mision Tic"
        
    }

@app.get("/usuarios/{user_id}")
def read_user(user_id: int):
    return {
        
        "user_id": user_id
        
    }


cursos = [

    {"cursos": "Fundamentos de programacion"},
    {"cursos": "Programacion Basica"},
    {"cursos": "Desarrollo de Software"},
    {"cursos": "Desarrollo Web"},

]

@app.get("/cursos")
def read_item(skip: int = 0, limit: int = 10):
    return cursos[skip: skip + limit]          
"""

#Methodos get

#ruta root
@app.get("/")
async def root():
    return {"message": "Hello World"}

#Path parametros  --> Obligatorios
@app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict:
    return {"item_id": item_id}


@app.get("/items/{item_id}/detail")
def show_item(
    item_id: int,
    name: str | None = Query(default=None, max_length=50),
    price: Optional[float] = Query(None, gt=0),
    description: Optional[str] = Query(None, min_length=1)
    ):

    #Interacion con la bd  
    return {
        'id': item_id,
        'nombre': name,
        'price': price,
        'descripcion': description
    }

#Base de datos simulada


fake_items_db = [{"item_name":"Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

#Query parametros --> opcionales
@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    #Traer informacion de la base de datos

    return fake_items_db[skip: skip + limit]

#Methodo Post
@app.post("/items/")
async def create_item(item: Item):
    #Logica de agregar item a la base de datos
    #Con el modelo de item

    return item

