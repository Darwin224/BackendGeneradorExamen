from pydantic import BaseModel
from datetime import date

# ---------- Tablas base ----------

class Persona(BaseModel):
    id: int
    nombre: str
    apellido: str
    sexo: str
    correo_electronico: str
    pais: str
    fecha_nacimiento: date

#Crear sin id porque es autogenerado
class PersonaCreate(BaseModel):
    nombre: str
    apellido: str
    sexo: str
    correo_electronico: str
    pais: str
    fecha_nacimiento: date

class Profesion(BaseModel):
    id: int
    nombre: str

#Crear sin id porque es autogenerado
class ProfesionCreate(BaseModel):
    nombre: str

class UsuarioFinal(BaseModel):
    id: int
    clave: str
    nombre_usuario: str
    profesion_id: int
    persona_id: int

#Crear sin id porque es autogenerado
class UsuarioFinalCreate(BaseModel):
    clave: str
    nombre_usuario: str
    profesion_id: int
    persona_id: int

# Para solicitudes Get
class UsuarioFinalRead(BaseModel):
    id: int
    clave: str
    nombre_usuario: str
    profesion: Profesion
    persona: Persona

class Empleado(BaseModel):
    id: int
    direccion: str
    persona_id: int

#Crear sin id porque es autogenerado
class EmpleadoCreate(BaseModel):
    direccion: str
    persona_id: int

class Permiso(BaseModel):
    id: int
    nombre: str

#Crear sin id porque es autogenerado
class PermisoCreate(BaseModel):
    nombre: str

class UsuarioAdministrativo(BaseModel):
    id: int
    clave: str
    nombre_usuario: str
    empleado_id: int
    permiso_id: int
#Crear sin id porque es autogenerado
class UsuarioAdministrativoCreate(BaseModel):
    clave: str
    nombre_usuario: str
    empleado_id: int
    permiso_id: int

# Para solicitudes Get
class UsuarioAdministrativoRead(BaseModel):
    id: int
    clave: str
    nombre_usuario: str
    empleado: Empleado
    permiso: Permiso
