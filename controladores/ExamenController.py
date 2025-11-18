from db.conexion import supabase
from modelos.ExamenModel import (
    MateriaCreate, CategoriaDePreguntaCreate, CategoriaDeSeccionCreate,
    ExamenCreate, SeccionExamenCreate, EncabezadoCreate
)

# ---------- Materia ----------
def crearMateria(materia: MateriaCreate):
    return supabase.schema("examen").table("materia").insert(materia.model_dump()).execute().data

def obtenerMaterias():
    return supabase.schema("examen").table("materia").select("*").execute().data

# ---------- CategoriaDePregunta ----------
def crearCategoriaDePregunta(categoria: CategoriaDePreguntaCreate):
    return supabase.schema("examen").table("categoriaDePregunta").insert(categoria.model_dump()).execute().data

def obtenerCategoriasDePregunta():
    return supabase.schema("examen").table("categoriaDePregunta").select("*").execute().data

# ---------- CategoriaDeSeccion ----------
def crearCategoriaDeSeccion(categoria: CategoriaDeSeccionCreate):
    return supabase.schema("examen").table("categoriaDeSeccion").insert(categoria.model_dump()).execute().data

def obtenerCategoriasDeSeccion():
    return supabase.schema("examen").table("categoriaDeSeccion").select("*").execute().data

# ---------- Examen ----------
def crearExamen(examen: ExamenCreate):
    return supabase.schema("examen").table("examen").insert(examen.model_dump()).execute().data

def obtenerExamenes():
    return supabase.schema("examen").table("examen").select("*, materia(*)").execute().data

# ---------- SeccionExamen ----------
def crearSeccionExamen(seccion: SeccionExamenCreate):
    return supabase.schema("examen").table("seccionExamen").insert(seccion.model_dump()).execute().data

def obtenerSeccionesExamen():
    return supabase.schema("examen").table("seccionExamen").select("*, categoriaDeSeccion(*), categoriaDePregunta(*)").execute().data

# ---------- Encabezado ----------
def crearEncabezado(encabezado: EncabezadoCreate):
    return supabase.schema("examen").table("encabezado").insert(encabezado.model_dump()).execute().data

def obtenerEncabezados():
    return supabase.schema("examen").table("encabezado").select("*").execute().data
