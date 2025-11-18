def construir_prompt(tipo, materia, tematica, cantidad, contenido_pdf):
    return f"""
Genera EXACTAMENTE {cantidad} preguntas del tipo: {tipo}.
No generes ningún otro tipo de pregunta.
Si el tipo es completación, entonces TODAS las preguntas deben ser de completación.

Materia: {materia}
Temática/Unidad: {tematica}

Formato esperado por tipo:

Si el tipo es "mixta":
- Debes generar preguntas: de opción múltiple, de verdadero/falso y de completación.
- Distribuye las {cantidad} preguntas en partes iguales entre los formatos.
- NO mezcles formatos dentro de una pregunta.
- Usa siempre "Respuesta correcta: X" solo para opción múltiple.
- Usa "( ) Verdadero" o "( ) Falso" en V/F.
- Usa "Respuesta: ..." en completación.


- Opción múltiple:
  - Cada pregunta debe comenzar con "**Pregunta X:**"
  - Debe tener 4 opciones: A), B), C), D)
  - Al final de cada pregunta, incluye una línea con "Respuesta correcta: X"

- Verdadero/Falso:
  - Cada pregunta debe comenzar con "**Pregunta X:**"
  - El enunciado debe terminar con "( ) Verdadero" o "( ) Falso"

- Completación:
  - Cada pregunta debe comenzar con "**Pregunta X:**"
  - El enunciado debe contener un espacio en blanco "______"
  - Al final, incluye una línea con "Respuesta: ..." (NO usar "Respuesta correcta")

Reglas estrictas:
- NO mezcles formatos.
- NO generes preguntas repetidas.
- NO uses "Respuesta correcta" en completación.
- SE RIGUROSO CON LOS FORMATOS.
- Usa exclusivamente el formato correspondiente al tipo indicado.
- El número total de preguntas debe ser EXACTAMENTE {cantidad}.

Contenido del PDF:
{contenido_pdf}
"""
