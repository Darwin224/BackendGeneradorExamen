from db.conexion import supabase
from modelos.ExamenModel import (
    MateriaCreate, CategoriaDePreguntaCreate, CategoriaDeSeccionCreate,
    ExamenCreate, SeccionExamenCreate, EncabezadoCreate
)


from fastapi import HTTPException
from modelos.ExamenModel import ExamenCreate, SeccionExamenCreate

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





#-------------------Gemini------------------------#


def save_exam_controller(examen_data: dict):
    try:
        # 1. Guardar examen principal
        examen_create = ExamenCreate(
            puntajeExamen=examen_data.get("puntajeExamen", 0),
            FKusuarioFinalID=examen_data["FKusuarioFinalID"],
            FKmateriaID=examen_data["FKmateriaID"]
        )

        res_exam = supabase.table("examen").insert({
            "puntaje_examen": examen_create.puntajeExamen,
            "usuario_final_id": examen_create.FKusuarioFinalID,
            "materia_id": examen_create.FKmateriaID
        }).execute()

        if res_exam.error:
            raise Exception(res_exam.error.message)

        examen_id = res_exam.data[0]["PKexamenID"]

        # 2. Guardar secciones/preguntas
        secciones = examen_data.get("secciones", [])
        secciones_data = [
            {
                "CFKexamenID": examen_id,
                "seccionDireccionArchivo": s["seccionDireccionArchivo"],
                "FKcategoriaDeSeccionID": s["FKcategoriaDeSeccionID"],
                "FKcategoriaDePreguntaID": s["FKcategoriaDePreguntaID"]
            }
            for s in secciones
        ]
        if secciones_data:
            res_sec = supabase.table("seccion_examen").insert(secciones_data).execute()
            if res_sec.error:
                raise Exception(res_sec.error.message)

        return {"message": "Examen guardado correctamente", "examen_id": examen_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
