from pydantic import BaseModel

class geminiModel(BaseModel):
    promt: str
    materia: str
    tematica: str
    tipoPregunta: str
    cantidadPreguntas: str
    
class Question(BaseModel):
    tipo_pregunta: str
    pregunta: str
    respuesta_correcta: str

class Exam(BaseModel):
    titulo: str
    profesor: str
    fecha: str
    cantidadPreguntas: int
    estado: str
    examen: list[Question]