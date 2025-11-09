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

import re

def parse_verdadero_falso(texto: str) -> list:
    preguntas = []

    # Captura bloques que comienzan con "**Pregunta N:**"
    pattern = re.compile(r"\*\*Pregunta\s+\d+\:\*\*\s*(.*?)(?=(\*\*Pregunta\s+\d+\:\*\*)|$)", re.DOTALL | re.IGNORECASE)
    for m in pattern.finditer(texto):
        bloque = m.group(1).strip()
        if not bloque:
            continue

        # Buscar enunciado seguido de "Verdadero" o "Falso", permitiendo "( )" antes
        match = re.search(r"(.*?)(\(\s*\)|)\s*(\bVerdadero\b|\bFalso\b)\.?\s*$", bloque, re.IGNORECASE)
        if not match:
            match = re.search(r"(.*?)(\(\s*\)|)\s*(\bVerdadero\b|\bFalso\b)", bloque, re.IGNORECASE)
        if not match:
            continue

        enunciado = (match.group(1) + (" " + match.group(2).strip() if match.group(2).strip() else "")).strip()
        respuesta = match.group(3).capitalize()

        # Filtrar enunciados demasiado cortos
        if len(enunciado.split()) < 3:
            continue

        preguntas.append({
            "pregunta": enunciado,
            "respuesta_correcta": respuesta
        })

    return preguntas




import re

def parse_completacion(texto: str) -> list:
    """
    Extrae preguntas de completación en bloques que comienzan con "**Pregunta N:**"
    Devuelve lista de dicts: {"pregunta": <enunciado>, "respuesta_correcta": <respuesta> or None, "error": <mensaje> (opcional)}
    Maneja ruido posterior (por ejemplo, texto del prompt concatenado).
    """
    preguntas = []

    # Normalizar saltos de línea
    texto = texto.replace('\r\n', '\n')

    # Capturar cada bloque que comienza con "**Pregunta N:**" hasta el siguiente o EOF
    pattern = re.compile(
        r"\*\*Pregunta\s+\d+\:\*\*\s*(.*?)(?=(\*\*Pregunta\s+\d+\:\*\*)|$)",
        re.DOTALL | re.IGNORECASE
    )

    for m in pattern.finditer(texto):
        bloque = m.group(1).strip()
        if not bloque:
            continue

        # Evitar que texto extra (por ejemplo, la función construir_prompt pegada) sea interpretado
        # Si el bloque contiene líneas que claramente no pertenecen a la pregunta (como "def construir_prompt("), ignorar desde ahí
        bloque = re.split(r"\bdef\s+construir_prompt\b", bloque, flags=re.IGNORECASE)[0].strip()

        # Buscar "Respuesta:" y separar enunciado y respuesta
        match = re.search(r"(.*?)(?:\n+)\s*Respuesta\s*:\s*(.+)$", bloque, re.IGNORECASE | re.DOTALL)
        if match:
            enunciado = match.group(1).strip()
            respuesta = match.group(2).strip()
            respuesta = respuesta if respuesta else None

            # Filtrar enunciados demasiado cortos (posible ruido)
            if len(enunciado.split()) < 3:
                preguntas.append({
                    "pregunta": enunciado,
                    "respuesta_correcta": respuesta,
                    "error": "Enunciado demasiado corto"
                })
                continue

            preguntas.append({
                "pregunta": enunciado,
                "respuesta_correcta": respuesta
            })
        else:
            # No se encontró "Respuesta:" en el bloque — intentar extraer respuesta en línea final
            inline_match = re.search(r"^(.*\S)\s*\n*$", bloque, re.DOTALL)
            if inline_match:
                enunciado_guess = inline_match.group(1).strip()
            else:
                enunciado_guess = bloque

            # Si no existe "Respuesta:", marcar para revisión
            if len(enunciado_guess.split()) < 3:
                continue

            preguntas.append({
                "pregunta": enunciado_guess,
                "respuesta_correcta": None,
                "error": "Formato incompleto: falta 'Respuesta:'"
            })

    return preguntas
