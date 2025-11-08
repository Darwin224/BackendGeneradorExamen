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


import re

def parse_verdadero_falso(texto: str) -> list:
    preguntas = []

    # Buscar bloques que comiencen explícitamente con "**Pregunta N:**" y capturarlos
    pattern = re.compile(r"\*\*Pregunta\s+\d+\:\*\*\s*(.*?)(?=(\*\*Pregunta\s+\d+\:\*\*)|$)", re.DOTALL | re.IGNORECASE)
    for m in pattern.finditer(texto):
        bloque = m.group(1).strip()
        if not bloque:
            continue

        # Buscar enunciado seguido de "Verdadero" o "Falso"
        match = re.search(r"(.*?)(\bVerdadero\b|\bFalso\b)\.?\s*$", bloque, re.IGNORECASE)
        if not match:
            # Intentar también si la respuesta está en la misma línea sin punto final
            match = re.search(r"(.*?)(\bVerdadero\b|\bFalso\b)", bloque, re.IGNORECASE)
        if not match:
            continue

        enunciado = match.group(1).strip()
        respuesta = match.group(2).capitalize()

        # Filtrar enunciados demasiado cortos (probables encabezados o ruido)
        if len(enunciado.split()) < 3:
            continue

        preguntas.append({
            "pregunta": enunciado,
            "respuesta_correcta": respuesta
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
