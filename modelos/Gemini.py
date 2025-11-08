from pydantic import BaseModel

class geminiModel(BaseModel):
    promt: str
    materia: str
    tematica: str
    tipoPregunta: str
    cantidadPreguntas: str
    
