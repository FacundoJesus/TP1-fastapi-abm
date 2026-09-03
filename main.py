from fastapi import FastAPI
from routers import users

# Creo la instancia de aplicacion
app = FastAPI()

# Router a endpoints user
app.include_router(users.router)

# Defino la ruta GET para la URL de la ruta
@app.get("/")
def read_root():
    return {"message": "Trabajo Práctico ABM + FastApi"}