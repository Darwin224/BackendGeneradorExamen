from db.conexion import supabase
from modelos.UsuarioModel import (
    PersonaCreate, ProfesionCreate, UsuarioFinalCreate,
    EmpleadoCreate, PermisoCreate, UsuarioAdministrativoCreate
)

# ---------- Persona ----------
def crearPersona(persona: PersonaCreate):
    data = persona.dict()
    data["fecha_nacimiento"] = data["fecha_nacimiento"].isoformat()  # 👈 conversión necesaria
    return supabase.table("persona").insert(data).execute().data


def obtenerPersonas():
    return supabase.table("persona").select("*").execute().data

# ---------- Profesion ----------
def crearProfesion(profesion: ProfesionCreate):
    return supabase.table("profesion").insert(profesion.dict()).execute().data

def obtenerProfesiones():
    return supabase.table("profesion").select("*").execute().data

# ---------- UsuarioFinal ----------
def crearUsuarioFinal(usuario: UsuarioFinalCreate):
    return supabase.table("usuarioFinal").insert(usuario.dict()).execute().data

def obtenerUsuariosFinales():
    return supabase.table("usuarioFinal").select("*, profesion(*), persona(*)").execute().data

# ---------- Empleado ----------
def crearEmpleado(empleado: EmpleadoCreate):
    return supabase.table("empleado").insert(empleado.dict()).execute().data

def obtenerEmpleados():
    return supabase.table("empleado").select("*").execute().data

# ---------- Permiso ----------
def crearPermiso(permiso: PermisoCreate):
    return supabase.table("permiso").insert(permiso.dict()).execute().data

def obtenerPermisos():
    return supabase.table("permiso").select("*").execute().data

# ---------- UsuarioAdministrativo ----------
def crearUsuarioAdministrativo(usuario: UsuarioAdministrativoCreate):
    return supabase.table("usuarioAdministrativo").insert(usuario.dict()).execute().data

def obtenerUsuariosAdministrativos():
    return supabase.table("usuarioAdministrativo").select("*, empleado(*), permiso(*)").execute().data
