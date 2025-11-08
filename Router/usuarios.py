from fastapi import APIRouter, Form
from pydantic import BaseModel
#from db.conexion import obtenerProductos
# from modelos.UsuarioModel import locales
from modelos.Gemini import geminiModel


#from controladores.UsusarioController2 import *
from controladores.gemini import geminiGenerador
from controladores.extraerTexto import extraer_texto_pdf

from fastapi import UploadFile, File



router = APIRouter()

# class User(BaseModel):
#     id: int
#     name: str
#     email: str
#     tel: str

# @router.get("/hola/{name}")
# def hola(name:str):
#     return a.saludar(name)


# @router.get("/crearUsuario/{usuario}")
# def crearUsuario(usuario:str, id: int):
#     id= str(id)
#     return a.crearUsuario(usuario)+ id

# @router.post("/crearUsuario2/")
# def crearUsuario2(user:User):
#     return user


# @router.get("/probar-db")
# def probar_db():
#     fecha = obtener_base()
#     if fecha:
#         return {"fecha_actual": str(fecha)}
#     return {"error": "No se pudo conectar a la base de datos"}

# @router.get("/obtenerProductos")
# def ObtenerProductos():
#     return obtenerProductos()

# @router.post("/crearLocal")
# def crearLocal(local: locales):
#     return crearProducto(local)

@router.post("/gemini")
def generar_respuesta(prompt: geminiModel):
    resultado = geminiGenerador(prompt.promt)
    return {"respuesta": resultado}

#####################################################

PROMPT_FIJO = """
Redacta un examen de opción múltiple basado en el siguiente contenido.
Incluye 10 preguntas, cada una con 4 opciones. Marca la respuesta correcta.
"""



@router.post("/generarExamenDesdePDF")
async def generar_examen_desde_pdf(
    archivo: UploadFile = File(...),
    promt: str = Form(...),
    materia: str = Form(...),
    tematica: str = Form(...),
    tipoPregunta: str = Form(...),
    cantidadPreguntas: str = Form(...)
):
    contenido_pdf = await extraer_texto_pdf(archivo)


    prompt_completo = f"""
Redacta un examen de {tipoPregunta} basado en el siguiente contenido.

Materia: {materia}
Temática: {tematica}
Cantidad de preguntas: {cantidadPreguntas}

Instrucción general: {promt}

Contenido del PDF:
{contenido_pdf}
"""

    respuesta = geminiGenerador(prompt_completo)
    return {"examen": respuesta}