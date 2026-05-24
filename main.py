from fastapi import FastAPI

app = FastAPI()

# Endpoint principal
@app.get("/")
def inicio():
    return {
        "mensaje": "Este es el proyecto de clientes a desarrollar"
    }

# Endpoint clientes
@app.get("/clientes")
def clientes():

    lista_clientes = [
        {
            "id": 1,
            "nombre": "Camilo Villaruel"
        },
        {
            "id": 2,
            "nombre": "Mateo Palacios"
        },
        {
            "id": 3,
            "nombre": "Silvana Estrada"
        }
    ]

    return {
        "clientes": lista_clientes
    }

# Endpoint saludar con nombre
@app.get("/saludar/{nombre}")
def saludar(nombre: str):

    return {
        "mensaje": f"Hola {nombre}"
    }

# Endpoint nombre y apellido
@app.get("/saludar/{nombre}/{apellido}")
def saludo_completo(nombre: str, apellido: str):

    return {
        "mensaje": f"Hola {nombre} {apellido}"
    }

# Endpoint con query parameter
@app.get("/saludar/{nombre}/{apellido}")
def saludo_edad(nombre: str, apellido: str, edad: int):

    return {
        "mensaje": f"Hola {nombre} {apellido}",
        "edad": edad
    }