from pydantic import BaseModel
from datetime import date

# ---------- Tablas base ----------

class Materia(BaseModel):
    id: int  # antes PKmateriaID
    nombre: str  # antes nombreDeMateria

class MateriaCreate(BaseModel):
    nombre: str

class CategoriaDePregunta(BaseModel):
    id: int  # antes PKcategoriaDePreguntaID
    nombre: str  # antes nombreCategoriDePregunta

class CategoriaDePreguntaCreate(BaseModel):
    nombre: str

class CategoriaDeSeccion(BaseModel):
    id: int  # antes PKcategoriaDeSeccionID
    nombre: str  # antes nombreCategoriDeSeccion
    materia_id: int  # antes FKmateria

class CategoriaDeSeccionCreate(BaseModel):
    nombre: str
    materia_id: int

class Examen(BaseModel):
    id: int  # antes PKexamenID
    puntaje_examen: int
    usuario_final_id: int  # antes FKusuarioFinalID
    materia_id: int  # antes FKmateriaID

class ExamenCreate(BaseModel):
    puntaje_examen: int
    usuario_final_id: int
    materia_id: int

class SeccionExamen(BaseModel):
    id: int  # antes CPKseccionExamenID
    examen_id: int  # antes CFKexamenID
    seccion_direccion_archivo: str
    categoria_de_seccion_id: int  # antes FKcategoriaDeSeccionID
    categoria_de_pregunta_id: int  # antes FKcategoriaDePreguntaID

class SeccionExamenCreate(BaseModel):
    examen_id: int
    seccion_direccion_archivo: str
    categoria_de_seccion_id: int
    categoria_de_pregunta_id: int

class Encabezado(BaseModel):
    id: int  # antes CPKencabezadoID
    usuario_id: int  # antes CFKusuarioID
    nombre_institucion: str
    direccion_logo_institucion: str
    departamento_educativo: str

class EncabezadoCreate(BaseModel):
    usuario_id: int
    nombre_institucion: str
    direccion_logo_institucion: str
    departamento_educativo: str

# ---------- Modelos para solicitudes GET con joins ----------

# Para GET con join: seccionExamen + categoriaDeSeccion + categoriaDePregunta
class SeccionExamenRead(BaseModel):
    id: int
    examen_id: int
    seccion_direccion_archivo: str
    categoria_de_seccion: CategoriaDeSeccion  # ← join con categoriaDeSeccion
    categoria_de_pregunta: CategoriaDePregunta  # ← join con categoriaDePregunta

# Para GET con join: examen + materia
class ExamenRead(BaseModel):
    id: int
    puntaje_examen: int
    usuario_final_id: int
    materia: Materia  # ← join con materia

# Para GET con join: encabezado + usuario
class EncabezadoRead(BaseModel):
    id: int
    nombre_institucion: str
    direccion_logo_institucion: str
    departamento_educativo: str
    usuario_id: int  # puedes anidar usuario si haces join
