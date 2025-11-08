from fastapi import APIRouter
from modelos.ExamenModel import (
    MateriaCreate, CategoriaDePreguntaCreate, CategoriaDeSeccionCreate,
    ExamenCreate, SeccionExamenCreate, EncabezadoCreate
)
from controladores.ExamenController import (
    crearMateria, obtenerMaterias,
    crearCategoriaDePregunta, obtenerCategoriasDePregunta,
    crearCategoriaDeSeccion, obtenerCategoriasDeSeccion,
    crearExamen, obtenerExamenes,
    crearSeccionExamen, obtenerSeccionesExamen,
    crearEncabezado, obtenerEncabezados
)

router = APIRouter()

# ---------- Materia ----------
@router.post("/crearMateria")
def ruta_crear_materia(materia: MateriaCreate):
    return crearMateria(materia)

@router.get("/obtenerMaterias")
def ruta_obtener_materias():
    return obtenerMaterias()

# ---------- CategoriaDePregunta ----------
@router.post("/crearCategoriaDePregunta")
def ruta_crear_categoria_pregunta(categoria: CategoriaDePreguntaCreate):
    return crearCategoriaDePregunta(categoria)

@router.get("/obtenerCategoriasDePregunta")
def ruta_obtener_categorias_pregunta():
    return obtenerCategoriasDePregunta()

# ---------- CategoriaDeSeccion ----------
@router.post("/crearCategoriaDeSeccion")
def ruta_crear_categoria_seccion(categoria: CategoriaDeSeccionCreate):
    return crearCategoriaDeSeccion(categoria)

@router.get("/obtenerCategoriasDeSeccion")
def ruta_obtener_categorias_seccion():
    return obtenerCategoriasDeSeccion()

# ---------- Examen ----------
@router.post("/crearExamen")
def ruta_crear_examen(examen: ExamenCreate):
    return crearExamen(examen)

@router.get("/obtenerExamenes")
def ruta_obtener_examenes():
    return obtenerExamenes()

# ---------- SeccionExamen ----------
@router.post("/crearSeccionExamen")
def ruta_crear_seccion_examen(seccion: SeccionExamenCreate):
    return crearSeccionExamen(seccion)

@router.get("/obtenerSeccionesExamen")
def ruta_obtener_secciones_examen():
    return obtenerSeccionesExamen()

# ---------- Encabezado ----------
@router.post("/crearEncabezado")
def ruta_crear_encabezado(encabezado: EncabezadoCreate):
    return crearEncabezado(encabezado)

@router.get("/obtenerEncabezados")
def ruta_obtener_encabezados():
    return obtenerEncabezados()
