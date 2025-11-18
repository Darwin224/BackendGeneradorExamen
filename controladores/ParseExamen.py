import re

def parse_examen_gemini(texto: str, tipo: str) -> list:
    tipo = tipo.lower().strip()
    preguntas = []

    # Procesar todos los tipos que estén mencionados en el string
    if "opcion" in tipo or "seleccion" in tipo or "multiple" in tipo:
        preguntas += parse_opcion_multiple(texto)
    if "verdadero" in tipo or "falso" in tipo or "vf" in tipo:
        preguntas += parse_verdadero_falso(texto)
    if "completacion" in tipo or "rellenar" in tipo:
        preguntas += parse_completacion(texto)

    if not preguntas:
        return [{"error": f"No se encontraron preguntas válidas para el tipo: {tipo}"}]

    return preguntas


def parse_opcion_multiple(texto: str) -> list:
    preguntas = []
    bloques = re.split(r"\*\*Pregunta\s+\d+\:\*\*", texto.strip())

    for bloque in bloques:
        bloque = bloque.strip()
        if not bloque:
            continue

        opciones = re.findall(r"([A-D]\)\s*.*)", bloque)
        respuesta_match = re.search(r"Respuesta correcta:\s*([A-D])", bloque)
        respuesta_correcta = respuesta_match.group(1) if respuesta_match else None

        if len(opciones) != 4 or not respuesta_correcta:
            continue

        pregunta_match = re.search(r"(.*?)A\)", bloque, re.DOTALL)
        pregunta = pregunta_match.group(1).strip() if pregunta_match else "Pregunta no encontrada"
        pregunta_completa = pregunta + '\n' + '\n'.join(opciones)

        preguntas.append({
            "tipo_pregunta": "opcion_multiple",
            "pregunta": pregunta_completa,
            "respuesta_correcta": respuesta_correcta
        })

    return preguntas


def parse_verdadero_falso(texto: str) -> list:
    preguntas = []
    pattern = re.compile(r"\*\*Pregunta\s+\d+\:\*\*\s*(.*?)(?=(\*\*Pregunta\s+\d+\:\*\*)|$)", re.DOTALL | re.IGNORECASE)

    for m in pattern.finditer(texto):
        bloque = m.group(1).strip()
        if not bloque or not re.search(r"\b(Verdadero|Falso)\b", bloque, re.IGNORECASE):
            continue

        # Ignorar bloques que contienen opciones tipo A), B), C), D)
        if re.search(r"[A-D]\)", bloque):
            continue

        # Ignorar bloques que parecen verdadero/falso pero no tienen formato válido
        if re.search(r"\b(Verdadero|Falso)\b", bloque) and "Respuesta:" not in bloque and not re.search(r"\(\s*\)", bloque):
            continue

        match = re.search(r"(.*?)(\(\s*\)|)\s*(\bVerdadero\b|\bFalso\b)\.?\s*$", bloque, re.IGNORECASE)
        if not match:
            match = re.search(r"(.*?)(\(\s*\)|)\s*(\bVerdadero\b|\bFalso\b)", bloque, re.IGNORECASE)
        if not match:
            continue

        enunciado = (match.group(1) + (" " + match.group(2).strip() if match.group(2).strip() else "")).strip()
        respuesta = match.group(3).capitalize()

        if len(enunciado.split()) < 3:
            continue

        preguntas.append({
            "tipo_pregunta": "verdadero_falso",
            "pregunta": enunciado,
            "respuesta_correcta": respuesta
        })

    return preguntas


def parse_completacion(texto: str) -> list:
    preguntas = []
    texto = texto.replace('\r\n', '\n')
    pattern = re.compile(r"\*\*Pregunta\s+\d+\:\*\*\s*(.*?)(?=(\*\*Pregunta\s+\d+\:\*\*)|$)", re.DOTALL | re.IGNORECASE)

    for m in pattern.finditer(texto):
        bloque = m.group(1).strip()

        # Ignorar preguntas que parecen verdadero/falso
        if re.search(r"\(\s*\)\s*(Verdadero|Falso)", bloque, re.IGNORECASE):
            continue

# Ignorar bloques que contienen opciones tipo A), B), C), D)
        if re.search(r"[A-D]\)", bloque):
            continue

# Ignorar bloques que usan "Respuesta correcta" en lugar de "Respuesta:"
        if "Respuesta correcta:" in bloque:
            continue


        # Ignorar bloques que contienen opciones tipo A), B), C), D)
        if re.search(r"[A-D]\)", bloque):
            continue

    # Ignorar bloques que usan "Respuesta correcta" en lugar de "Respuesta:"
        if "Respuesta correcta:" in bloque:
            continue

        if not bloque:
            continue

        bloque = re.split(r"\bdef\s+construir_prompt\b", bloque, flags=re.IGNORECASE)[0].strip()
        match = re.search(r"(.*?)(?:\n+)\s*Respuesta\s*:\s*(.+)$", bloque, re.IGNORECASE | re.DOTALL)

        if match:
            enunciado = match.group(1).strip()
            respuesta = match.group(2).strip()
            if len(enunciado.split()) < 3:
                continue

            preguntas.append({
                "tipo_pregunta": "completacion",
                "pregunta": enunciado,
                "respuesta_correcta": respuesta
            })
        else:
            inline_match = re.search(r"^(.*\S)\s*\n*$", bloque, re.DOTALL)
            enunciado_guess = inline_match.group(1).strip() if inline_match else bloque

            if len(enunciado_guess.split()) < 3:
                continue

            preguntas.append({
                "tipo_pregunta": "completacion",
                "pregunta": enunciado_guess,
                "respuesta_correcta": None,
                "error": "Formato incompleto: falta 'Respuesta:'"
            })

    return preguntas
