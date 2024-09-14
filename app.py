# Importamos las bibliotecas necesarias
from fastapi import FastAPI

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Definir un endpoint para la raíz con método GET
@app.get("/")
def home():
    # Retorna un simple mensaje de texto
    return 'Hola mundo: Model API - VERSION 1'