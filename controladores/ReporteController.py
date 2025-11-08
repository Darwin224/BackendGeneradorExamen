from db.conexion import supabase
from modelos.ReporteModel import (
    DatosUsuarioFinalCreate, ReporteCreate,
    DatoDePaisCreate, DatoDeTemaCreate
)

# ---------- DatosUsuarioFinal ----------
def crearDatosUsuarioFinal(datos: DatosUsuarioFinalCreate):
    return supabase.table("datosUsuarioFinal").insert(datos.dict()).execute().data

def obtenerDatosUsuarioFinales():
    return supabase.table("datosUsuarioFinal").select("*").execute().data

# ---------- Reporte ----------
def crearReporte(reporte: ReporteCreate):
    data = reporte.dict()
    data["fecha_reporte"] = data["fecha_reporte"].isoformat()
    return supabase.table("reporte").insert(data).execute().data


def obtenerReportes():
    return supabase.table("reporte").select("*, datosUsuarioFinal(*)").execute().data

# ---------- DatoDePais ----------
def crearDatoDePais(dato: DatoDePaisCreate):
    return supabase.table("datoDePais").insert(dato.dict()).execute().data

def obtenerDatosDePais():
    return supabase.table("datoDePais").select("*, reporte(*)").execute().data

# ---------- DatoDeTema ----------
def crearDatoDeTema(dato: DatoDeTemaCreate):
    return supabase.table("datoDeTema").insert(dato.dict()).execute().data

def obtenerDatosDeTema():
    return supabase.table("datoDeTema").select("*, reporte(*)").execute().data
