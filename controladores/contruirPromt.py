def construir_prompt(tipo, materia, tematica, cantidad, puntaje, contenido_pdf):
    return f"""
Redacta un examen de tipo {tipo} basado en el siguiente contenido.

Materia: {materia}
Temática/Unidad: {tematica}
Cantidad de preguntas: {cantidad}
Puntaje total: {puntaje}

Formato esperado:
- Si es opción múltiple:
  - Cada pregunta debe comenzar con "**Pregunta X:**"
  - Debe tener 4 opciones: A), B), C), D)
  - Al final de cada pregunta, incluye una línea con "Respuesta correcta: X"
  - Ejemplo:
    **Pregunta 1:**
    ¿Qué es ITIL?
    A) Un marco de gestión de servicios
    B) Un lenguaje de programación
    C) Un sistema operativo
    D) Un protocolo de red
    Respuesta correcta: A

- Si es verdadero/falso:
  - Cada pregunta debe comenzar con "**Pregunta X:**"
  - Enunciado seguido de "Verdadero" o "Falso"
  - Ejemplo:
    **Pregunta 1:**
    ITIL es un marco de gestión de servicios. Verdadero

- Si es completación:
  - Cada pregunta debe comenzar con "**Pregunta X:**"
  - Enunciado con espacio en blanco
  - Al final, incluye una línea con "Respuesta: ..."
  - Ejemplo:
    **Pregunta 1:**
    El marco de gestión de servicios más utilizado en TI es ______.
    Respuesta: ITIL

Contenido del PDF:
{contenido_pdf}
"""
