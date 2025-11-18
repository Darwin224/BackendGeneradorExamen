from pydantic import BaseModel
from datetime import date

from typing import Optional

# ---------- Tablas base ----------

class Persona(BaseModel):
    id: int
    nombre: str
    apellido: str
    sexo: bool
    correoElectronico: str
    pais: str
    fechaDeNacimiento: date

#Crear sin id porque es autogenerado
class PersonaCreate(BaseModel):
    nombre: str
    apellido: str
    sexo: bool
    correoElectronico: str
    pais: str
    fechaDeNacimiento: date

class Profesion(BaseModel):
    PKprofesionID: int
    nombre: str

#Crear sin id porque es autogenerado
class ProfesionCreate(BaseModel):
    nombre: str

class UsuarioFinal(BaseModel):
    PKusuarioFinalID: int
    claveUsuarioFinal: str
    nombreUsuarioFinal: str
    FKprofesionID: int
    FKpersonaID: int

#Crear sin id porque es autogenerado
class UsuarioFinalCreate(BaseModel):
    claveUsuarioFinal: str
    nombreUsuarioFinal: str
    FKprofesionID: int
    FKpersonaID: int

# Para solicitudes Get
class UsuarioFinalRead(BaseModel):
    id: int
    clave: str
    nombre_usuario: str
    profesion: Profesion
    persona: Persona

class Empleado(BaseModel):
    PKempleadoID: int
    direccionEmpleado: str
    FKpersonaID: int

#Crear sin id porque es autogenerado
class EmpleadoCreate(BaseModel):
    direccionEmpleado: str
    FKpersonaID: int

class Permiso(BaseModel):
    PKpermisoID: int
    nombrePermiso: str

#Crear sin id porque es autogenerado
class PermisoCreate(BaseModel):
    nombrePermiso: str

class UsuarioAdministrativo(BaseModel):
    PKusuarioAdministrativoID: int
    claveUsuarioAdministrativo: str
    nombreUsuarioAdministrativo: str
    FKempleadoID: int
    FKpermisoID: int
#Crear sin id porque es autogenerado
class UsuarioAdministrativoCreate(BaseModel):
    claveUsuarioAdministrativo: str
    nombreUsuarioAdministrativo: str
    FKempleadoID: int
    FKpermisoID: int

# Para solicitudes Get
class UsuarioAdministrativoRead(BaseModel):
    PKusuarioAdministrativoID: int
    claveUsuarioAdministrativo: str
    nombreUsuarioAdministrativo: str
    FKempleadoID: int
    FKpermisoID: int
