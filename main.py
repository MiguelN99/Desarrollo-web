from fastapi import FastAPI

app = FastAPI()

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
