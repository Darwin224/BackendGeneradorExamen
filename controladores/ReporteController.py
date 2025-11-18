from db.conexion import supabase
from modelos.ReporteModel import (
    DatosUsuarioFinalCreate, ReporteCreate,
    DatoDePaisCreate, DatoDeTemaCreate
)

# ---------- DatosUsuarioFinal ----------
def crearDatosUsuarioFinal(datos: DatosUsuarioFinalCreate):
    return supabase.schema("reporte").table("datoDeUsuarioFinal").insert(datos.model_dump()).execute().data

def obtenerDatosUsuarioFinales():
    return supabase.schema("reporte").table("datoDeUsuarioFinal").select("*").execute().data

# ---------- Reporte ----------
def crearReporte(reporte: ReporteCreate):
    data = reporte.model_dump()
    data["fecha_reporte"] = data["fecha_reporte"].isoformat()
    return supabase.schema("reporte").table("reporte").insert(data).execute().data


def obtenerReportes():
    return supabase.schema("reporte").table("reporte").select("*").execute().data

# ---------- DatoDePais ----------
def crearDatoDePais(dato: DatoDePaisCreate):
    return supabase.schema("reporte").table("datoDePais").insert(dato.model_dump()).execute().data

def obtenerDatosDePais():
    return supabase.schema("reporte").table("datoDePais").select("*, reporte(*)").execute().data

# ---------- DatoDeTema ----------
def crearDatoDeTema(dato: DatoDeTemaCreate):
    return supabase.schema("reporte").table("datoDeTema").insert(dato.model_dump()).execute().data

def obtenerDatosDeTema():
    return supabase.schema("reporte").table("datoDeTema").select("*, reporte(*)").execute().data
