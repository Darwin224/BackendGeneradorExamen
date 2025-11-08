from fastapi import APIRouter
from modelos.ReporteModel import (
    DatosUsuarioFinalCreate, ReporteCreate,
    DatoDePaisCreate, DatoDeTemaCreate
)
from controladores.ReporteController import (
    crearDatosUsuarioFinal, obtenerDatosUsuarioFinales,
    crearReporte, obtenerReportes,
    crearDatoDePais, obtenerDatosDePais,
    crearDatoDeTema, obtenerDatosDeTema
)

router = APIRouter()

# ---------- DatosUsuarioFinal ----------
@router.post("/crearDatosUsuarioFinal")
def ruta_crear_datos_usuario_final(datos: DatosUsuarioFinalCreate):
    return crearDatosUsuarioFinal(datos)

@router.get("/obtenerDatosUsuarioFinales")
def ruta_obtener_datos_usuario_finales():
    return obtenerDatosUsuarioFinales()

# ---------- Reporte ----------
@router.post("/crearReporte")
def ruta_crear_reporte(reporte: ReporteCreate):
    return crearReporte(reporte)

@router.get("/obtenerReportes")
def ruta_obtener_reportes():
    return obtenerReportes()

# ---------- DatoDePais ----------
@router.post("/crearDatoDePais")
def ruta_crear_dato_de_pais(dato: DatoDePaisCreate):
    return crearDatoDePais(dato)

@router.get("/obtenerDatosDePais")
def ruta_obtener_datos_de_pais():
    return obtenerDatosDePais()

# ---------- DatoDeTema ----------
@router.post("/crearDatoDeTema")
def ruta_crear_dato_de_tema(dato: DatoDeTemaCreate):
    return crearDatoDeTema(dato)

@router.get("/obtenerDatosDeTema")
def ruta_obtener_datos_de_tema():
    return obtenerDatosDeTema()
