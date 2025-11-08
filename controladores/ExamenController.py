from db.conexion import supabase
from modelos.ExamenModel import (
    MateriaCreate, CategoriaDePreguntaCreate, CategoriaDeSeccionCreate,
    ExamenCreate, SeccionExamenCreate, EncabezadoCreate
)

# ---------- Materia ----------
def crearMateria(materia: MateriaCreate):
    return supabase.table("materia").insert(materia.dict()).execute().data

def obtenerMaterias():
    return supabase.table("materia").select("*").execute().data

# ---------- CategoriaDePregunta ----------
def crearCategoriaDePregunta(categoria: CategoriaDePreguntaCreate):
    return supabase.table("categoriaDePregunta").insert(categoria.dict()).execute().data

def obtenerCategoriasDePregunta():
    return supabase.table("categoriaDePregunta").select("*").execute().data

# ---------- CategoriaDeSeccion ----------
def crearCategoriaDeSeccion(categoria: CategoriaDeSeccionCreate):
    return supabase.table("categoriaDeSeccion").insert(categoria.dict()).execute().data

def obtenerCategoriasDeSeccion():
    return supabase.table("categoriaDeSeccion").select("*").execute().data

# ---------- Examen ----------
def crearExamen(examen: ExamenCreate):
    return supabase.table("examen").insert(examen.dict()).execute().data

def obtenerExamenes():
    return supabase.table("examen").select("*, materia(*)").execute().data

# ---------- SeccionExamen ----------
def crearSeccionExamen(seccion: SeccionExamenCreate):
    return supabase.table("seccionExamen").insert(seccion.dict()).execute().data

def obtenerSeccionesExamen():
    return supabase.table("seccionExamen").select("*, categoriaDeSeccion(*), categoriaDePregunta(*)").execute().data

# ---------- Encabezado ----------
def crearEncabezado(encabezado: EncabezadoCreate):
    return supabase.table("encabezado").insert(encabezado.dict()).execute().data

def obtenerEncabezados():
    return supabase.table("encabezado").select("*").execute().data
