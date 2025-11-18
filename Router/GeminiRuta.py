from fastapi import APIRouter, Form, UploadFile, File, Body
from typing import List
from datetime import date
from controladores.ExamenController import save_exam_controller
from controladores.ParseExamen import parse_examen_gemini
from controladores.contruirPromt import construir_prompt
from controladores.gemini import geminiGenerador
from controladores.extraerTexto import extraer_texto_pdf

router = APIRouter()

@router.post("/generarExamenDesdePDF")
async def generar_examen_desde_pdf(
    archivo: UploadFile = File(...),
    materia: str = Form(...),
    tematica: str = Form(...),
    tipoPregunta: List[str] = Form(...),  # ← checkbox como lista
    cantidadPreguntas: str = Form(...)
):
    # Extraer texto del PDF
    contenido_pdf = await extraer_texto_pdf(archivo)

    # Unificar tipos seleccionados en un solo string
    tipo_unificado = " ".join(tipoPregunta).lower().replace(",", " ").replace("/", " ").strip()

    # Si el usuario selecciona 'mixto' o algún tipo no reconocido, mapear a todos los tipos
    tipos_validos = ["opcion_multiple", "verdadero_falso", "completacion"]
    if "mixto" in tipo_unificado or not any(t in tipo_unificado for t in tipos_validos):
        tipo_unificado = " ".join(tipos_validos)

    # Construir el prompt para Gemini
    prompt_completo = construir_prompt(
        tipo_unificado, materia, tematica, cantidadPreguntas, contenido_pdf
    )

    # Generar texto con Gemini
    respuesta = geminiGenerador(prompt_completo)

    # Parsear el examen según los tipos seleccionados
    examen_raw = parse_examen_gemini(respuesta, tipo_unificado)

    # Formatear al JSON que espera el frontend
    # Formatear al JSON que espera el frontend
    examen_formateado = [
        {
            "tipo": q.get("tipo_pregunta", "desconocido"),
            "pregunta": q.get("pregunta", ""),
            "respuesta_correcta": q.get("respuesta_correcta", "")  # <-- cambia 'respuesta' por 'respuesta_correcta'
    }
    for q in examen_raw
    if "error" not in q
]

   # print(examen_formateado)
    return {
        "examen": examen_formateado,
        "titulo": f"Examen - {materia}",
        "profesor": "Ingrese su nombre",
        "fecha": date.today().isoformat()
    }

@router.post("/save")
def save_exam_route(examen: dict = Body(...)):
    """
    Recibe un JSON con la estructura de examen y lo guarda en Supabase.
    """
    return save_exam_controller(examen)
