import re

def parse_examen_gemini(texto: str, tipo: str) -> list:
    tipo = tipo.lower().strip()

    if tipo in ["selección", "seleccion", "opción múltiple", "opcion multiple", "multiple"]:
        return parse_opcion_multiple(texto)
    elif tipo in ["v o f", "verdadero/falso", "verdadero o falso", "vf"]:
        return parse_verdadero_falso(texto)
    elif tipo in ["completacion", "completación", "rellenar"]:
        return parse_completacion(texto)
    else:
        return [{"error": f"Tipo de pregunta no reconocido: {tipo}"}]

def parse_opcion_multiple(texto: str) -> list:
    preguntas = []
    
    # Separar por encabezados tipo "**Pregunta X:**"
    bloques = re.split(r"\*\*Pregunta\s+\d+\:\*\*", texto.strip())

    for bloque in bloques:
        if not bloque.strip():
            continue

        # Buscar opciones completas incluyendo la letra
        opciones = re.findall(r"([A-D]\)\s*.*)", bloque)
        respuesta_match = re.search(r"Respuesta correcta:\s*([A-D])", bloque)
        respuesta_correcta = respuesta_match.group(1) if respuesta_match else None

        # Validar que haya 4 opciones y una respuesta
        if len(opciones) != 4 or not respuesta_correcta:
            continue

        # Extraer la pregunta antes de A)
        pregunta_match = re.search(r"(.*?)A\)", bloque, re.DOTALL)
        pregunta = pregunta_match.group(1).strip() if pregunta_match else "Pregunta no encontrada"

        preguntas.append({
            "pregunta": pregunta,
            "opciones": opciones,
            "respuesta_correcta": respuesta_correcta
        })

    return preguntas



def parse_verdadero_falso(texto: str) -> list:
    preguntas = []
    bloques = re.split(r"\n\s*\d+\.\s", texto.strip())

    for bloque in bloques:
        match = re.match(r"(.*?)(Verdadero|Falso)", bloque.strip(), re.IGNORECASE)
        if match:
            pregunta = match.group(1).strip()
            respuesta = match.group(2).capitalize()
            preguntas.append({
                "pregunta": pregunta,
                "respuesta_correcta": respuesta
            })
        else:
            preguntas.append({
                "pregunta": bloque.strip(),
                "respuesta_correcta": None,
                "error": "Formato incompleto"
            })

    return preguntas

def parse_completacion(texto: str) -> list:
    preguntas = []
    bloques = re.split(r"\n\s*\d+\.\s", texto.strip())

    for bloque in bloques:
        match = re.match(r"(.*?)\s*Respuesta:\s*(.*)", bloque.strip())
        if match:
            enunciado = match.group(1).strip()
            respuesta = match.group(2).strip()
            preguntas.append({
                "enunciado": enunciado,
                "respuesta_correcta": respuesta
            })
        else:
            preguntas.append({
                "enunciado": bloque.strip(),
                "respuesta_correcta": None,
                "error": "Formato incompleto"
            })

    return preguntas
