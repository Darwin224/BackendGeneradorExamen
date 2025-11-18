from db.conexion import supabase
from modelos.UsuarioModel import (
    PersonaCreate, ProfesionCreate, UsuarioFinalCreate,
    EmpleadoCreate, PermisoCreate, UsuarioAdministrativoCreate
)

# ---------- Persona ----------
def crearPersona(persona: PersonaCreate):
    data = persona.model_dump()
    data["fechaDeNacimiento"] = data["fechaDeNacimiento"].isoformat()  # 👈 conversión necesaria
    return supabase.schema("usuario").table("persona").insert(data).execute().data


def obtenerPersonas():
    return supabase.schema("usuario").table("persona").select("*").execute().data

# ---------- Profesion ----------
def crearProfesion(profesion: ProfesionCreate):
    return supabase.schema("usuario").table("profesion").insert(profesion.model_dump()).execute().data

def obtenerProfesiones():
    return supabase.schema("usuario").table("profesion").select("*").execute().data

# ---------- UsuarioFinal ----------
def crearUsuarioFinal(usuario: UsuarioFinalCreate):
    return supabase.schema("usuario").table("usuarioFinal").insert(usuario.model_dump()).execute().data

def obtenerUsuariosFinales():
    return supabase.schema("usuario").table("usuarioFinal").select("*, profesion(*), persona(*)").execute().data

# ---------- Empleado ----------
def crearEmpleado(empleado: EmpleadoCreate):
    return supabase.schema("usuario").table("empleado").insert(empleado.model_dump()).execute().data

def obtenerEmpleados():
    return supabase.schema("usuario").table("empleado").select("*").execute().data

# ---------- Permiso ----------
def crearPermiso(permiso: PermisoCreate):
    return supabase.schema("usuario").table("permiso").insert(permiso.model_dump()).execute().data

def obtenerPermisos():
    return supabase.schema("usuario").table("permiso").select("*").execute().data

# ---------- UsuarioAdministrativo ----------
def crearUsuarioAdministrativo(usuario: UsuarioAdministrativoCreate):
    return supabase.schema("usuario").table("usuarioAdministrativo").insert(usuario.model_dump()).execute().data

def obtenerUsuariosAdministrativos():
    return supabase.schema("usuario").table("usuarioAdministrativo").select("*, empleado(*), permiso(*)").execute().data
