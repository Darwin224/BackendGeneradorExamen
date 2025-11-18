from pydantic import BaseModel
from datetime import date

# ---------- Tablas base ----------

class Materia(BaseModel):
    PKmateriaID: int  # antes PKmateriaID
    nombreDeMateria: str  # antes nombreDeMateria

class MateriaCreate(BaseModel):
    nombreDeMateria: str

class CategoriaDePregunta(BaseModel):
    PKcategoriaDePregunta: int 
    nombreCategoriaDePregunta: str 

class CategoriaDePreguntaCreate(BaseModel):
    nombreCategoriaDePregunta: str

class CategoriaDeSeccion(BaseModel):
    PKcategoriaDeSeccionID: int  # antes PKcategoriaDeSeccionID
    nombreCategoriaDeSeccion: str  # antes nombreCategoriDeSeccion
    FKmateriaID: int  # antes FKmateria

class CategoriaDeSeccionCreate(BaseModel):
    nombreCategoriaDeSeccion: str
    FKmateriaID: int

class Examen(BaseModel):
    PKexamenID: int  
    puntajeExamen: int
    FKusuarioFinalID: int 
    FKmateriaID: int  

class ExamenCreate(BaseModel):
    puntajeExamen: int
    FKusuarioFinalID: int
    FKmateriaID: int

class SeccionExamen(BaseModel):
    CPKseccionExamenID: int 
    CFKexamenID: int 
    seccionDireccionArchivo: str
    FKcategoriaDeSeccionID: int 
    FKcategoriaDePreguntaID: int 

class SeccionExamenCreate(BaseModel):
    CFKexamenID: int 
    seccionDireccionArchivo: str
    FKcategoriaDeSeccionID: int 
    FKcategoriaDePreguntaID: int 

class Encabezado(BaseModel):
    CPKencabezadoID: int  # antes CPKencabezadoID
    CFKusuarioFinalID: int  # antes CFKusuarioID
    nombreInstitucion: str
    direccionLogoInstitucion: str
    departamentoEducativo: str

class EncabezadoCreate(BaseModel):
    CFKusuarioFinalID: int  # antes CFKusuarioID
    nombreInstitucion: str
    direccionLogoInstitucion: str
    departamentoEducativo: str

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
