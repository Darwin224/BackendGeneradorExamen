# servicios/pdf.py
from fastapi import UploadFile
import fitz  # PyMuPDF
async def extraer_texto_pdf(file: UploadFile) -> str:
    contenido = await file.read()  # ✅ esto sí es awaitable
    doc = fitz.open(stream=contenido, filetype="pdf")
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()
    return texto
